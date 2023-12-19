# AutoLogin
北师大专用，自动登录网络。这个py文件可以设置开机自动运行

# 关于运行计划
1. 设置登录后启动、按时启动等 2. 设置启动失败后的重复启动次数 3. 如有必要，可以设置延迟启动 4. 确保计划可以成功运行
5. 相关设置的选项：a. Run only when user is logged on b. Run with highest privileges c. Configure for Win10 d. 确保脚本有足够的运行权限
6. 给PC设置来电自启，防止断电导致主机没有自动启动。




# window10设置自动登录。主要是考虑断电重启后的运行，因为如果不自动登录，那么脚本运作问题暂时无法解决。
## 不用的时候锁屏即可，别注销，不应该计划执行。


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
# 其他
可以保留360安全卫士，断网急救箱，修复异常网络问题，比如DNS异常导致网页无法访问。或者其他离线网络修复工具。


