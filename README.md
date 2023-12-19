# AutoLogin
北师大专用，自动登录网络。这个py文件可以设置开机自动运行

# 关于运行计划
1. 设置登录后启动、按时启动等 2. 设置启动失败后的重复启动次数 3. 如有必要，可以设置延迟启动 4. 确保计划可以成功运行

# window10取消自动登录

1，按WIN+R键，输入control userpasswords2，回车

2，在弹出画面里，取消勾选【要使用本计算机，用户必须输入用户名和密码】

3，点击确定，输入密码

但是现在升级到最新版的win10以后，第二步的选择框不见了。

解决方法：

1，按WIN+R键，输入regedit，回车

2，在注册表里找到这个路径：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device

3，找到DevicePasswordLessBuildVersion，双击打开

4，显示的值应该是2。改成0，点击确定。

然后再按WIN+R键，输入control userpasswords2，回车，就会消失的选择框回来了。
