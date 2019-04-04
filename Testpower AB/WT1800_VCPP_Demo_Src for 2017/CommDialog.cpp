/*==========================================================
 Copyright (C) 2005 YOKOGAWA ELECTRIC CORPORATION

    ALL RIGHTS RESERVED BY YOKOGAWA ELECTRIC CORPORATION.
THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT
WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND/OR FITNESS FOR A PARTICULAR PURPOSE.

                            YOKOGAWA ELECTRIC CORPORATION
==========================================================*/
// CommDialog.cpp

#include "stdafx.h"
#include "WT1800Demo.h"
#include "CommDialog.h"
#include "MainDialog.h"
#include "Connection.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

const CString GPIB_ADDR[] = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16",
                             "17","18","19","20","21","22","23","24","25","26","27","28","29","30"};

/////////////////////////////////////////////////////////////////////////////
// CCommDialog

CCommDialog::CCommDialog(CWnd* pParent /*=NULL*/)
	: CDialog(CCommDialog::IDD, pParent)
{
	//m_connection = NULL;
	//{{AFX_DATA_INIT(CCommDialog)
	m_iWire = -1;
	//}}AFX_DATA_INIT
}


void CCommDialog::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CCommDialog)
	DDX_Control(pDX, IDC_COMBO_ADDR, m_comboAddr);
	DDX_Radio(pDX, IDC_RADIO_GPIB, m_iWire);
	//}}AFX_DATA_MAP
	DDX_Control(pDX, IDC_CMB_SERIALNO, Cmbbox_SerialNo);
	DDX_Control(pDX, IDC_CMB_IPADDR, Cmbbox_IPAddr);
	DDX_Control(pDX, IDC_EDIT_SERIALNO, m_Edit_SerialNo);
	DDX_Control(pDX, IDC_EDIT_IPADDR, m_Edit_IPAddr);
	DDX_Control(pDX, IDC_BTN_SEARCH_USBTMC, m_Btn_SearchSerialNo);
	DDX_Control(pDX, IDC_BTN_SEARCH_ETHER, m_Btn_SearchIPAddr);
}

BEGIN_MESSAGE_MAP(CCommDialog, CDialog)
	//{{AFX_MSG_MAP(CCommDialog)
	ON_BN_CLICKED(IDC_RADIO_GPIB, OnRadioGpib)
	ON_BN_CLICKED(IDC_RADIO_ETHER, OnRadioEther)
	ON_BN_CLICKED(IDC_RADIO_USB, OnRadioUsb)
	//}}AFX_MSG_MAP
//	ON_BN_CLICKED(IDOK, &CCommDialog::OnBnClickedOk)
	ON_BN_CLICKED(IDC_BTN_SEARCH_ETHER, &CCommDialog::OnBnClickedBtnSearchEther)
	ON_BN_CLICKED(IDC_BTN_SEARCH_USBTMC, &CCommDialog::OnBnClickedBtnSearchUsbtmc)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CCommDialog message handler

BOOL CCommDialog::OnInitDialog()
{
    m_hIcon = AfxGetApp()->LoadIcon(IDI_ICON);
	CDialog::OnInitDialog();
    //SetIcon(m_hIcon, FALSE);
    SetIcon(m_hIcon, TRUE);

    //set the list items into comboBoxs
	int i; 
	for (i=0; i<30; i++)
	{
		m_comboAddr.AddString(GPIB_ADDR[i]);
	}
	// set the default values of comboBox
	m_comboAddr.SetCurSel(0);
	GetConnectSettings();
	m_nEditOrCombo_Ether = 0;		//0:edit 1:combo
	m_nEditOrCombo_USB = 0;			//0:edit 1:combo

    UpdateData(false);
	// set the default selection as GPIB
	CButton* pBtn = (CButton*)GetDlgItem(IDC_RADIO_GPIB);
	pBtn->SetCheck(1);

    // Call GPIB RadioButton's event to refresh display.
	OnRadioGpib(); 

	return true;
}

void CCommDialog::OnRadioGpib() 
{
    //set GPIB options enable.
	m_comboAddr.EnableWindow(true);
	//set EtherNet options disable.
	Cmbbox_IPAddr.EnableWindow(false);
	m_Edit_IPAddr.EnableWindow(false);
	m_Btn_SearchIPAddr.EnableWindow(false);
 	//set usb options disable
	Cmbbox_SerialNo.EnableWindow(false);
	m_Edit_SerialNo.EnableWindow(false);
	m_Btn_SearchSerialNo.EnableWindow(false);
}

void CCommDialog::OnRadioUsb() 
{
	//set USB options enable
	if( m_nEditOrCombo_USB == 0){
	 	m_Edit_SerialNo.EnableWindow(true);
	}
	else
	{
		Cmbbox_SerialNo.EnableWindow(true);
	}
	m_Btn_SearchSerialNo.EnableWindow(true);
	//set GPIB options disable.
	m_comboAddr.EnableWindow(false);
    //set EtherNet options disable.
	Cmbbox_IPAddr.EnableWindow(false);
	m_Edit_IPAddr.EnableWindow(false);
	m_Btn_SearchIPAddr.EnableWindow(false);
}

void CCommDialog::OnRadioEther() 
{
	//set EtherNet options enable.
	if( m_nEditOrCombo_Ether == 0){
		m_Edit_IPAddr.EnableWindow(true);
	}
	else
	{
		Cmbbox_IPAddr.EnableWindow(true);
	}
	m_Btn_SearchIPAddr.EnableWindow(true);
	//set GPIB options disable.
	m_comboAddr.EnableWindow(false);
	//set usb options disable
	Cmbbox_SerialNo.EnableWindow(false);
	m_Edit_SerialNo.EnableWindow(false);
	m_Btn_SearchSerialNo.EnableWindow(false);
}

void CCommDialog::OnOK() 
{
	CString address;
	char encode[256];
	char usbSerialno[256];

	// get the checked one
	UINT nID = GetCheckedRadioButton(IDC_RADIO_GPIB,IDC_RADIO_ETHER);

    int tryAgain = IDOK;//when connection failed, ask for trying again.
    while(tryAgain == IDOK)
    {
        UpdateData();  //used for DDX refresh
	    switch (m_iWire)
	    {
		    case 0: // when GPIB was selected, set options into m_sAddress.
			    m_comboAddr.GetLBText(m_comboAddr.GetCurSel(),address);
			    m_connection.m_sAddress = address;
			    m_connection.m_iPort    = 1;
			    break;
		    case 1: // when EtherNet was selected, set options into m_sAddress.
                    //do not set user/passwd when no user name.
				if( m_nEditOrCombo_Ether == 0)
				{
					m_Edit_IPAddr.GetWindowText(m_connection.m_sAddress);
				}
				else
				{
					Cmbbox_IPAddr.GetWindowText(m_connection.m_sAddress);
				}
				m_connection.m_iPort    = 8;
			    break;
			case 2: //when usb was selected, set options into m_sAddres.
				if( m_nEditOrCombo_USB == 0){
					m_Edit_SerialNo.GetWindowText(address);
				}
				else
				{
					Cmbbox_SerialNo.GetWindowText(address);
				}
				strcpy_s(usbSerialno, address);
				m_connection.EncodeSerialNumber(encode, 256, usbSerialno);
				m_connection.m_sAddress.Format("%s",  encode);
			    m_connection.m_iPort = 7;
			    break;
	    }
	    // connect to the instrument
	    if (m_connection.Initialize() == 0)
        {
			WriteConnectSettings(m_iWire);
			CDialog::OnOK();
			return;
        }
        //display the asking dialog.
        tryAgain = MessageBox("Can not connect with the instrument, try again?", "Connection failed.", MB_OKCANCEL|MB_ICONERROR);
    }
}

void CCommDialog::GetConnectSettings()
{
	char	buff[16];

	//FilePath
	::GetModuleFileNameA(NULL,szFullPath,_MAX_PATH);
	_splitpath_s(szFullPath, szDrive, _MAX_DRIVE, szDir, _MAX_DIR, szFname, _MAX_FNAME, szExt, _MAX_EXT);
	Ini_Path.Format("%s%s%s.ini", szDrive, szDir, szFname);

	//GPIB_Address
	GetPrivateProfileString( Ini_Sec_Connect, Ini_Key_GPIB_Address,	"",buff, 16, Ini_Path);
	m_comboAddr.SelectString(-1,buff);

	//USB-TMC_SerialNo
	GetPrivateProfileString( Ini_Sec_Connect, Ini_Key_USB_Serial,	"",	buff, 16, Ini_Path);
	m_Edit_SerialNo.SetWindowText(buff);

	//IPAddress
	GetPrivateProfileString( Ini_Sec_Connect, Ini_Key_Ether_IPAddr,	"",	buff, 16, Ini_Path);
	m_Edit_IPAddr.SetWindowText(buff);
}

void CCommDialog::WriteConnectSettings(int m_iWire)
{
	CString addr;
	switch(m_iWire)
	{
		case 0:
			//GPIB_Address
			m_comboAddr.GetWindowText(addr);
			WritePrivateProfileString(Ini_Sec_Connect,	Ini_Key_GPIB_Address,	(LPCSTR)addr,	Ini_Path);
			break;
		case 1:
			//Ether_IPAddress
			if( m_nEditOrCombo_Ether == 0)
			{
				m_Edit_IPAddr.GetWindowText(addr);
			}
			else
			{
				Cmbbox_IPAddr.GetWindowText(addr);
			}
			WritePrivateProfileString(Ini_Sec_Connect,	Ini_Key_Ether_IPAddr,	(LPCSTR)addr,	Ini_Path);
			break;
		case 2:
			//USB_SerialNo
			if( m_nEditOrCombo_USB == 0)
			{
				m_Edit_SerialNo.GetWindowText(addr);
			}
			else
			{
				Cmbbox_SerialNo.GetWindowText(addr);
			}
			WritePrivateProfileString(Ini_Sec_Connect,	Ini_Key_USB_Serial,		(LPCSTR)addr,	Ini_Path);
			break;
	}
}

void CCommDialog::OnBnClickedBtnSearchEther()
{
	DEVICELIST	listbuff[127];
	DEVICELIST	list[127];
	int		n;
	int		ret ;
	int		num ;
	int		listindex = 0;

	ret = TmcSearchDevices(TM_CTL_VXI11, listbuff, 127, &num, NULL);

	for( n = 0; n < num; n++)
	{
		ret = Check_WTSeries(TM_CTL_VXI11,listbuff[n].adr);
		if (ret == 0)
		{
			list[listindex]=listbuff[n];
			listindex++;
		}
	}
	if(listindex > 0)
	{
		MessageBox("Device is found","Search Result",MB_ICONINFORMATION|MB_OK);
		if( 1 == listindex )
		{
			m_Edit_IPAddr.ShowWindow(true);
			Cmbbox_IPAddr.ShowWindow(false);
			m_Edit_IPAddr.SetWindowTextA(list[0].adr);
			m_nEditOrCombo_Ether = 0;
		}
		else
		{
			m_Edit_IPAddr.ShowWindow(false);
			Cmbbox_IPAddr.ShowWindow(true);
			Cmbbox_IPAddr.ResetContent();
			for(int n=0 ; n < listindex; n++)
			{
				Cmbbox_IPAddr.AddString(list[n].adr);
			}
			Cmbbox_IPAddr.SetCurSel(0);
			m_nEditOrCombo_Ether = 1;
		}
	}
	else
	{
		m_Edit_IPAddr.ShowWindow(true);
		Cmbbox_IPAddr.ShowWindow(false);
		m_Edit_IPAddr.SetWindowTextA("");
		Cmbbox_IPAddr.ResetContent();
		m_nEditOrCombo_Ether = 0;
		MessageBox("Device is not found","Search Result",MB_ICONINFORMATION|MB_OK);
	}
	OnRadioEther();
}

void CCommDialog::OnBnClickedBtnSearchUsbtmc()
{
	DEVICELIST	listbuff[127];
	DEVICELIST	list[127];
	int		n;
	int		num ;
	int		ret ;
	int		listindex = 0;
	char	decode[256] ;

#ifndef _OLDTMCTL
	ret = TmcSearchDevices(TM_CTL_USBTMC2, listbuff, 127, &num, NULL);
#else
	//DEVICELISTEX listbuffEx[127];
	//ret = TmcSearchDevicesEx(TM_CTL_USBTMC2, listbuffEx, 127, &num, NULL);

	//int max = num;
	//memset(listbuff, 0, sizeof(DEVICELIST)*127);

	//// devlist‚ð‹l‚ß‚é
	//int count = 0;
	//for (int i = 0; i < max; i++) {
	//	if (listbuffEx[i].adr[0] != NULL)
	//		memcpy(&listbuff[count++].adr[0], &listbuffEx[i].adr[0], ADRMAXLEN);
	//}
#endif // _OLDTMCTL

	for( n = 0; n < num; n++)
	{
		ret = Check_WTSeries(TM_CTL_USBTMC2,listbuff[n].adr);
		if (ret == 0)
		{
			list[listindex]=listbuff[n];
			listindex++;
		}
	}
	if(listindex > 0 )
	{
		MessageBox("Device is found","Search Result",MB_ICONINFORMATION|MB_OK);
		if(1 == listindex)
		{
			m_Edit_SerialNo.ShowWindow(true);
			Cmbbox_SerialNo.ShowWindow(false);
			ret = TmcDecodeSerialNumber(decode,256,list[0].adr);
			if( ret == 0 && decode != NULL )
			{
				m_Edit_SerialNo.SetWindowTextA(decode);
			}
			m_nEditOrCombo_USB = 0;
		}
		else
		{
			Cmbbox_SerialNo.ShowWindow(true);
			m_Edit_SerialNo.ShowWindow(false);
			Cmbbox_SerialNo.ResetContent();
			for(int n=0; n < listindex; n++ )
			{
				ret = TmcDecodeSerialNumber(decode,256,list[n].adr);
				if( ret == 0 && decode != NULL )
				{
					Cmbbox_SerialNo.AddString(decode);
				}
			}
			Cmbbox_SerialNo.SetCurSel(0);
			m_nEditOrCombo_USB = 1;
		}
	}
	else
	{
		m_Edit_SerialNo.ShowWindow(true);
		Cmbbox_SerialNo.ShowWindow(false);
		m_Edit_SerialNo.SetWindowTextA("");
		Cmbbox_SerialNo.ResetContent();
		m_nEditOrCombo_USB = 0;
		MessageBox("Device is not found","Search Result",MB_ICONINFORMATION|MB_OK);
	}
	OnRadioUsb();
}

int CCommDialog::Check_WTSeries(int wire,char* addr)
{
	CString m_sAddr = addr;
	CString m_sName;
	int ret;
	int		m_iID;

	ret = TmcInitialize(wire, m_sAddr.GetBuffer(0), &m_iID);
	//ret = TmcInitializeEx(wire, m_sAddr.GetBuffer(0), &m_iID, 1);
	if(ret != 0)
	{
		return ret;
	}
	//tmcsetterm
	ret = TmcSetTerm(m_iID, 2, 1);
	if(ret != 0)
	{
		TmcFinish(m_iID);
		return ret;
	}
	//tmcsettimeout(1*100ms)
	ret = TmcSetTimeout(m_iID, 1);
	if(ret != 0)
	{
		TmcFinish(m_iID);
		return ret;
	}
	//test the device module connected.
	ret = TmcSend(m_iID, "*IDN?");
	int maxLength = 256;
	char* buf ;
	if ((buf = new char[maxLength]) == NULL)
	{
		TmcSetTimeout( m_iID, 300 );
		TmcFinish(m_iID);
		return 1;
	}
	memset(buf,0,maxLength);
	int realLength;
	ret = TmcReceive(m_iID, buf, maxLength, &realLength);
	m_sName.Format("%s", buf);
	delete[] buf;
	if(ret != 0)
	{
		TmcFinish(m_iID);
	}
	ret = m_sName.Find("WT18",0);
	if(ret == -1)
	{
		ret = 1;
	}
	else{
		ret = 0;
	}
	//tmcsettimeout(50*100ms)
	TmcSetTimeout( m_iID, 50 );
	TmcFinish(m_iID);
	return ret;
}
