/*==========================================================
 Copyright (C) 2005 YOKOGAWA ELECTRIC CORPORATION

    ALL RIGHTS RESERVED BY YOKOGAWA ELECTRIC CORPORATION.
THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT
WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND/OR FITNESS FOR A PARTICULAR PURPOSE.

                            YOKOGAWA ELECTRIC CORPORATION
==========================================================*/
// WT1800Demo.h : WT1800DEMO

#if !defined(AFX_WT1800DEMO_H__4BEA790E_226B_4CAE_A9C5_93FC0758B2A9__INCLUDED_)
#define AFX_WT1800DEMO_H__4BEA790E_226B_4CAE_A9C5_93FC0758B2A9__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"
#include "Connection.h"

/////////////////////////////////////////////////////////////////////////////
// CWT1800DemoApp: reference class defination with .cpp file

class CWT1800DemoApp : public CWinApp
{
public:
	CWT1800DemoApp();
	//CDevice* m_pDevice;

	//{{AFX_VIRTUAL(CWT1800DemoApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

	//{{AFX_MSG(CWT1800DemoApp)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}

#endif // !defined(AFX_WT1800DEMO_H__4BEA790E_226B_4CAE_A9C5_93FC0758B2A9__INCLUDED_)
