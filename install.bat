@echo off
echo "�뽫���ص��ķ����ļ��϶����˴��󰴻س�(Enter)"
set /p "inputfile="
echo "��ȷ���ļ�����"

: inputv
echo "��׼ȷ��������GitKraken�汾��(�����ֵ�����)�����»س������"
echo 8.2.1
set /p "vvvv="
echo "������İ汾��%vvvv%"
echo "��ȷ���Ƿ���ȷ����ȷ����1�����»س����ķ��������������ݣ���������汾��"
set /p "choseemm="

if %choseemm% == 1 (
	echo "���ں���..."
	copy /y %inputfile% %localappdata%\gitkraken\app-%vvvv%\resources\app.asar.unpacked\src\strings.json
	echo "Done!"
	echo "5����˳�..."
	ping -n 5 127.1 >nul
	exit
)else (
	goto inputv
)



