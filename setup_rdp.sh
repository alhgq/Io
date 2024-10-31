#!/bin/bash

# تحديث النظام وتثبيت xfce4 و xrdp
echo "تحديث النظام وتثبيت البرامج المطلوبة..."
sudo apt update && sudo apt upgrade -y
sudo apt install xfce4 xfce4-goodies xrdp -y

# تكوين xrdp لاستخدام xfce4
echo "تكوين xrdp لاستخدام xfce4..."
echo "xfce4-session" > ~/.xsession
sudo sed -i 's/^exec .*/exec startxfce4/' /etc/xrdp/xrdp.ini

# إعادة تشغيل خدمة xrdp
echo "إعادة تشغيل خدمة xrdp..."
sudo systemctl restart xrdp

# السماح بالاتصال عبر جدار الحماية
echo "السماح بالاتصال عبر جدار الحماية على المنفذ 3389..."
sudo ufw allow 3389/tcp

# تعيين كلمة مرور افتراضية للمستخدم الحالي إذا لم تكن موجودة
PASSWORD="8900"
echo "$PASSWORD" | sudo passwd --stdin "$(whoami)" &> /dev/null

# الحصول على تفاصيل الاتصال
IP_ADDRESS=$(curl -s http://checkip.amazonaws.com)
USERNAME=$(whoami)

# عرض تفاصيل الاتصال في التيرمنال
echo -e "\nتم إعداد RDP بنجاح! تفاصيل الاتصال:\n"
echo "IP Address: $IP_ADDRESS"
echo "Username: $USERNAME"
echo "Password: $PASSWORD"
echo -e "\nيمكنك الآن استخدام هذه التفاصيل للاتصال عبر Remote Desktop.\n"
