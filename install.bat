@echo off
echo "请将下载到的翻译文件拖动到此处后按回车(Enter)"
set /p "inputfile="
echo "请确认文件无误"

: inputv
echo "请准确输入您的GitKraken版本号(纯数字点的组合)，按下回车，如↓"
echo 8.2.1
set /p "vvvv="
echo "你输入的版本是%vvvv%"
echo "请确定是否正确，正确输入1，按下回车；的否则输入其他内容，重新输入版本号"
set /p "choseemm="

if %choseemm% == 1 (
	echo "正在汉化..."
	copy /y %inputfile% %localappdata%\gitkraken\app-%vvvv%\resources\app.asar.unpacked\src\strings.json
	echo "Done!"
	echo "5秒后退出..."
	ping -n 5 127.1 >nul
	exit
)else (
	goto inputv
)



