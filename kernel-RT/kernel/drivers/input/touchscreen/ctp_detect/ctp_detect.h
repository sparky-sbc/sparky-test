#ifndef _CTP_DETECT_H_
#define _CTP_DETECT_H_

struct ctp_device
{
	char * name;			//0.IC����
	char * ko_name; 		//1.ko����
	bool need_detect;		//2.�Ƿ�ɨ��
	unsigned int i2c_addr;	//3.i2c��ַ
	bool has_chipid;		//4.��chipid
	unsigned int chipid_req;//5.chipid�Ĵ���
	unsigned int chipid;	//6.chipid
};

//ÿ����һ��IC��������б������
struct ctp_device ctp_device_list[]=
{
//ע���������ic��i2c��ַ��ͬ������chipid�ķ���ǰ�档
	//ICN83XX
	{
		"ICN83XX",			//0.IC����
		"ctp_icn83xx.ko", //"ctp_icn838x_ts_iic.ko"	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x40,				//3.i2c��ַ
		true,				//4.��chipid
		0x0a,				//5.chipid�Ĵ���
		0x83,				//6.chipid
	},
	//GSL1680,GSL3670,GSL3680,��������ͨ������ͬ��һ�㲻����ã�
	//��1680��D��E�棬3680��A��B�棬chipid����ͬ��ȫ��ɨ��̫�鷳�����ﲻ�����֡�
	{
		"GSLX6X0",			//0.IC����
		"ctp_gslX680.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x40,				//3.i2c��ַ
		false,				//4.��chipid
		0xfc,					//5.chipid�Ĵ���
		0x0,//1680:0x0			//6.chipid
	},
	//FT5206,FT5406
	{
		"FT52-406",			//0.IC����
		"ctp_ft5X06.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x38,				//3.i2c��ַ
		true,				//4.��chipid
		0xA3,				//5.chipid�Ĵ���
		0x55,				//6.chipid
	},
	//FT5606
	{
		"FT5606",			//0.IC����
		"ctp_ft5X06.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x38,				//3.i2c��ַ
		true,				//4.��chipid
		0xA3,				//5.chipid�Ĵ���
		0x08,				//6.chipid
	},
	//GT813
	{
		"GT813",			//0.IC����
		"ctp_goodix_touch.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x5d,				//3.i2c��ַ
		true,				//4.��chipid
		0xf7d,				//5.chipid�Ĵ���
		0x13,				//6.chipid
	},
	//AW5206
	{
		"AW5206",			//0.IC����
		"ctp_aw5306.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x38,				//3.i2c��ַ
		true,				//4.��chipid
		0x01,				//5.chipid�Ĵ���
		0xA8,				//6.chipid
	},
	//AW5209
	{
		"AW5209",			//0.IC����
		"ctp_aw5209.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x38,				//3.i2c��ַ
		true,				//4.��chipid
		0x01,				//5.chipid�Ĵ���
		0xB8,				//6.chipid
	},
	//CT36X
	{
		"CT36X",			//0.IC����
		"ctp_ct36x_i2c_ts.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x01,				//3.i2c��ַ
		true,				//4.��chipid
		0x00,//???				//5.chipid�Ĵ���
		0x00,//0x02:CT360,0x01:CT363,CT365	//6.chipid
	},
	//HL3X06
	{
		"HL3X06",			//0.IC����
		"ctp_hl3x06.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x3B,				//3.i2c��ַ
		false,				//4.��chipid
		0x00,				//5.chipid�Ĵ���
		0x30,				//6.chipid
	},
	//ILITEK
	{
		"ILITEK",			//0.IC����
		"ctp_ilitek_aimvF.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x41,				//3.i2c��ַ
		false,	//ȷʵ��			//4.��chipid
		0,				//5.chipid�Ĵ���
		0,				//6.chipid
	},
	//ili2672
	{
		"ili2672",			//0.IC����
		"ctp_ili2672.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x41,				//3.i2c��ַ
		false,	//ȷʵ��			//4.��chipid
		0,				//5.chipid�Ĵ���
		0,				//6.chipid
	},
	//ft5x06
	{
		"ft5x06",			//0.IC����
		"ctp_ft5x06.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x38,				//3.i2c��ַ
		false,	//ȷʵ��			//4.��chipid
		0,				//5.chipid�Ĵ���
		0,				//6.chipid
	},	
	//MT395
	{
		"MT395",			//0.IC����
		"ctp_mt395.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x67,				//3.i2c��ַ
		false,				//4.��chipid
		0,				//5.chipid�Ĵ���
		0,				//6.chipid
	},	
	//NOVATEK
	{
		"NT1100X",			//0.IC����
		"ctp_Novatek_TouchDriver.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x01,				//3.i2c��ַ
		false,				//4.��chipid
		0x00,	//???		//5.chipid�Ĵ���
		0,	//???			//6.chipid
	},	
	//SSD254X
	{
		"SSD254X",			//0.IC����
		"ctp_ssd254x.ko",	//1.ko����
		true,				//2.�Ƿ�ɨ��
		0x48,				//3.i2c��ַ
		true,				//4.��chipid
		0x02,					//5.chipid�Ĵ���
		0x25,	//0x2541,0x2543			//6.chipid
	},		
};


#endif
