/*==========================================================
 Copyright (C) 2005 YOKOGAWA ELECTRIC CORPORATION

    ALL RIGHTS RESERVED BY YOKOGAWA ELECTRIC CORPORATION.
THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT
WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND/OR FITNESS FOR A PARTICULAR PURPOSE.

                            YOKOGAWA ELECTRIC CORPORATION
==========================================================*/
// WT1800Demo.cpp

#include "stdafx.h"
#include "WT1800Demo.h"
#include "CommDialog.h"
#include "MainDialog.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CWT1800DemoApp

BEGIN_MESSAGE_MAP(CWT1800DemoApp, CWinApp)
	//{{AFX_MSG_MAP(CWT1800DemoApp)
	//}}AFX_MSG
	ON_COMMAND(ID_HELP, CWinApp::OnHelp)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CWT1800DemoApp instructor

CWT1800DemoApp::CWT1800DemoApp()
{
}

/////////////////////////////////////////////////////////////////////////////
//CWT1800DemoApp object

CWT1800DemoApp theApp;

/////////////////////////////////////////////////////////////////////////////
// CWT1800DemoApp initialize

BOOL CWT1800DemoApp::InitInstance()
{
	AfxEnableControlContainer();

#ifdef _AFXDLL
//	Enable3dControls();
#else
	Enable3dControlsStatic();
#endif
	CCommDialog commDlg;
	int nResponse = commDlg.DoModal();
    if (nResponse != IDOK)
	{
		return false;
	}
	CMainDialog mainDlg;
	nResponse = mainDlg.DoModal();
	//if currentdirectoryconnect
	return false;
}
