from django.test import TestCase

# Create your tests here.
products = [
  {
    'id': 1.1, 
    'productId': 'phones',
    'name': 'Apple iPhone 11 64 GB', 
    'price': 499.9, 
    'description': 'The iPhone 11 is a smartphone designed, developed, and marketed by Apple Inc. It is the 13th generation, lower-priced iPhone, succeeding the iPhone XR. The prominent changes compared with the iPhone XR are the Apple A13 Bionic chip, and an ultra-wide dual-camera system.', 
    'imageUrl': 'https://m.media-amazon.com/images/I/71kZfQA-Y7L._AC_UY218_.jpg',
    'rating': 4.8,
    'shareLink': 'https://www.amazon.com/Apple-Carrier-Subscription-Cricket-Wireless/dp/B084GSFQYW/ref=sr_1_1?dchild=1&keywords=Iphone+11&qid=1614520397&sr=8-1',
    'likes': 51
  }, 
  {
    'id': 1.2, 
    'productId': 'phones',
    'name': 'Apple iPhone 12 Pro 512 GB', 
    'price': 1099.9, 
    'description': 'Major upgrades over the iPhone 11 Pro and iPhone 11 Pro Max include the addition of 5G support, the LiDAR sensor, ProRAW (DNG) allowing high quality lossless 12bit image capture in the native photos app with the use of the new DNG v1.6 specification, the introduction of the MagSafe wireless charging and accessory system, the Apple A14 Bionic.', 
    'imageUrl': 'https://m.media-amazon.com/images/I/71YlH-4MUQL._AC_UY218_.jpg',
    'rating': 4.5,
    'shareLink': 'https://www.amazon.com/Apple-iPhone-Graphite-Carrier-Subscription/dp/B08L5QPVH7/ref=sr_1_2?dchild=1&keywords=Iphone+11&qid=1614520367&sr=8-2',
    'likes': 33
  },
  {
    'id': 1.3, 
    'productId': 'phones',
    'name': 'Samsung Galaxy S10 128GB+8GB RAM SM-G973F', 
    'price': 599.9, 
    'description': '6.1 inches QHD+ Dynamic AMOLED Infinity-O Display 1440 x 3040 pixels, 19:9 ratio (~550 ppi density) HDR10+ certified - Front/back glass (Gorilla Glass 6), aluminum frame - IP68 dust/water proof (up to 1.5m for 30 mins) > Not advised for beach or pool use - Android 9 (Pie). 128 GB + 8 GB RAM - microSD, up to 512 GB - 64-bit Octa-Core Processor - Ultrasonic Fingerprint sensor - Non-removable Li-Ion 3400 mAh battery.', 
    'imageUrl': 'https://m.media-amazon.com/images/I/61YVqHdFRxL._AC_UY218_.jpg',
    'rating': 4.7,
    'shareLink': 'https://www.amazon.com/Samsung-SM-G973F-DS-Smartphone-International/dp/B07NZXXZB2/ref=sr_1_5?dchild=1&keywords=samsung+galaxy+s10&qid=1614668229&sr=8-5',
    'likes': 26
  },
  {
    'id': 1.4, 
    'productId': 'phones',
    'name': 'Xiaomi Redmi Note 9S (128GB, 6GB)', 
    'price': 267.0, 
    'description': '6.67 inches, DotDisplay, FHD+, 1080 x 2400 pixels, 20:9 ratio, Corning Gorilla Glass 5, 450 nits typ. brightness. 64/128GB or 4/6GB RAM, Qualcomm SM7125 Snapdragon 720G, Octa-core Processor, Android 10, MIUI 11. Rear Camera: 48MP + 8MP + 5MP + 2MP, Front Camera: 16MP, 3.5mm jack, Bluetooth5.0, 5020 mAh battery.', 
    'imageUrl': 'https://m.media-amazon.com/images/I/61ySS-qrNYL._AC_UY218_.jpg',
    'rating': 4.5,
    'shareLink': 'https://www.amazon.com/Xiaomi-5020mAh-Unlocked-T-Mobile-International/dp/B085W9B2KH/ref=sr_1_2?dchild=1&keywords=Xiaomi+note+9&qid=1614697488&sr=8-2',
    'likes': 40
  },
  {
    'id': 1.5, 
    'productId': 'phones',
    'name': 'Samsung Galaxy Note 20 Ultra 5G 128GB', 
    'price': 1079.9, 
    'description': 'Display & Gaming: The best Galaxy mobile gaming and display experience yet; With a breathtaking screen refresh rate, adaptive Dynamic AMOLED 2X display, Galaxy 5G support & advanced processor, you get a smooth gaming experience with virtually no lag. HyperFast Processor: Multitask with Samsung’s fastest Note processor yet.', 
    'imageUrl': 'https://m.media-amazon.com/images/I/81NKXayE47L._AC_UY218_.jpg',
    'rating': 4.4,
    'shareLink': 'https://www.amazon.com/Samsung-Electronics-Unlocked-Smartphone-Long-Lasting/dp/B08BX7QGKF/ref=sr_1_1?dchild=1&keywords=Samsung+note+20&qid=1614697715&sr=8-1',
    'likes': 63
  },
  {
    'id': 2.1,
    'productId': 'tvs',
    'name': 'TCL 32S327 32-Inch 1080p Roku Smart LED TV',
    'price': 215.0,
    'description': '1080p Full HD Resolution excellent detail, color, and contrast. Wireless Connection: 802.11 2x2 Dual Band. Smart Functionality offers access to over 5,000 streaming channels featuring more than 500,000 movies and TV episodes via Roku TV.',
    'imageUrl': 'https://m.media-amazon.com/images/I/71Ut6ZxFbpL._AC_UL320_.jpg',
    'rating': 4.5,
    'shareLink': 'https://www.amazon.com/TCL-32S327-32-Inch-1080p-Smart/dp/B07F981R8M/ref=sr_1_1?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=SREFZAEZSX9R1FG29V2H&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1614698224&rnid=1266092011&s=electronics&sr=1-1',
    'likes': 55
  },
  {
    'id': 2.2,
    'productId': 'tvs',
    'name': 'SAMSUNG 85-inch Class Crystal UHD TU-8000',
    'price': 837.5,
    'description': 'CRYSTAL PROCESSOR 4K: This ultra-fast processor transforms everything you watch into stunning 4K. CRYSTAL DISPLAY: Experience crystal clear colors that are fine-tuned to deliver a naturally crisp and vivid picture.',
    'imageUrl': 'https://m.media-amazon.com/images/I/91FcuuZwcrL._AC_UL320_.jpg',
    'rating': 4.4,
    'shareLink': 'https://www.amazon.com/Samsung-85-inch-Crystal-TU-8000-Built/dp/B084JCFNHF/ref=sr_1_2?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=SREFZAEZSX9R1FG29V2H&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1614698224&rnid=1266092011&s=electronics&sr=1-2',
    'likes': 50
  },
  {
    'id': 2.3,
    'productId': 'tvs',
    'name': 'TCL 65" 5-Series 4K UHD Dolby Vision HDR QLED',
    'price': 569.9,
    'description': 'Superior 4K Ultra HD: Picture clarity combined with the contrast, color, and detail of Dolby Vision HDR (High Dynamic Range) for the most lifelike picture. QLED: Quantum dot technology delivers better brightness and wider color volume.',
    'imageUrl': 'https://m.media-amazon.com/images/I/91tMNAWWsPL._AC_UL320_.jpg',
    'rating': 4.5,
    'shareLink': 'https://www.amazon.com/TCL-Dolby-Vision-QLED-Smart/dp/B08857ZHY3/ref=sr_1_3?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=SREFZAEZSX9R1FG29V2H&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1614698224&rnid=1266092011&s=electronics&sr=1-3',
    'likes': 80
  },
  {
    'id': 2.4,
    'productId': 'tvs',
    'name': 'SAMSUNG QN32Q50RAFXZA Flat 32" QLED 4K',
    'price': 447.9,
    'description': '4K UHD Processor: a powerful processor optimizes your tv’ s performance with 4K picture quality. 4K UHD: see what you’ve been missing on a crisp, clear picture that’s 4x the resolution of Full HD. Inputs & Outputs: 3 HDMI ports, 1 Ethernet port, 2 USB Ports (v 2.0), 1 Digital Audio Output (Optical), 1 Composite Input (AV).',
    'imageUrl': 'https://m.media-amazon.com/images/I/51NKhnjhpGL._AC_UL320_.jpg',
    'rating': 4.6,
    'shareLink': 'https://www.amazon.com/SAMSUNG-QN32Q50RAFXZA-32Q50-Smart-TV2019/dp/B07W5QYD2K/ref=sr_1_5?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=SREFZAEZSX9R1FG29V2H&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1614698224&rnid=1266092011&s=electronics&sr=1-5',
    'likes': 98
  },
  {
    'id': 2.5,
    'productId': 'tvs',
    'name': 'SAMSUNG 65-inch Class QLED Q80T Series',
    'price': 749.9,
    'description': 'DIRECT FULL ARRAY 12X (85", 75", 65" & 55"): Controlled backlights offer deeper contrast for richer blacks and brighter whites. QUANTUM HDR 12X (85", 75", 65" & 55"): Fine-tuned shades of cinematic color make details leap off the screen. QUANTUM PROCESSOR 4K: This powerful processor uses deep learning AI to transform everything you watch into stunning 4K.',
    'imageUrl': 'https://m.media-amazon.com/images/I/61DIUfDxBtL._AC_UL320_.jpg',
    'rating': 4.6,
    'shareLink': 'https://www.amazon.com/SAMSUNG-65-inch-Class-QLED-Built/dp/B0845ZSMWS/ref=sr_1_8?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=SREFZAEZSX9R1FG29V2H&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1614698224&rnid=1266092011&s=electronics&sr=1-8',
    'likes': 80
  },
  {
    'id': 3.1,
    'productId': 'computers',
    'name': 'Kingston 240GB A400 SATA 3 2.5" Internal SSD',
    'price': 34.9,
    'description': 'Fast start up, loading and file transfers. More reliable and durable than a hard drive. Multiple capacities with space for applications or a hard drive replacement.',
    'imageUrl': 'https://m.media-amazon.com/images/I/91RL+MhTWbL._AC_UL320_.jpg',
    'rating': 4.9,
    'shareLink': 'https://www.amazon.com/Kingston-240GB-Solid-SA400S37-240G/dp/B01N5IB20Q/ref=sr_1_11?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=17Y4X0Q1VVDP4JH1KN1V&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1614699308&rnid=16225007011&s=computers-intl-ship&sr=1-11',
    'likes': 93
  },
  {
    'id': 3.2,
    'productId': 'computers',
    'name': 'AMD Ryzen 5 3600 6-Core, 12-Thread',
    'price': 228.0,
    'description': 'The world\'s most advanced processor in the desktop PC gaming segment. 6 cores and 12 processing threads bundled with the quiet AMD wraith stealth cooler max temps 95°C. 4,2 GHz max boost unlocked for overclocking 35 MB of game cache DDR4 3200 support.',
    'imageUrl': 'https://m.media-amazon.com/images/I/71WPGXQLcLL._AC_UL320_.jpg',
    'rating': 5.0,
    'shareLink': 'https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=sr_1_2?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=17Y4X0Q1VVDP4JH1KN1V&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1614699696&rnid=16225007011&s=computers-intl-ship&sr=1-2',
    'likes': 95
  },
  {
    'id': 3.3,
    'productId': 'computers',
    'name': 'Lenovo Yoga 9i 14 2-in-1 14\'',
    'price': 1399.0,
    'description': '11th Generation Intel Core i7-1185G7 Processor (3.00 GHz, up to 4.80 GHz with Turbo Boost, 4 Cores, 8 Threads, 12 MB Cache); 16GB Soldered LPDDR4x-4266 Memory; 512GB SSD M.2 2280 PCIe 3.0x4 NVMe. 14" FHD (1920x1080) IPS 400nits Glossy, Glass, 72% NTSC, Dolby Vision; Integrated Intel Iris Xe Graphics.',
    'imageUrl': 'https://m.media-amazon.com/images/I/41Rjr+67OtL._AC_UL320_.jpg',
    'rating': 4.4,
    'shareLink': 'https://www.amazon.com/Lenovo-Touch-Screen-Platform-i7-1185G7-16GB-Built/dp/B08QH1C5PY/ref=sr_1_11?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=17Y4X0Q1VVDP4JH1KN1V&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1614699855&rnid=16225007011&s=computers-intl-ship&sr=1-11',
    'likes': 66
  },
  {
    'id': 3.4,
    'productId': 'computers',
    'name': 'Dell Precision 3000 3640 Workstation',
    'price': 1461.9,
    'description': 'Core i7 i7-10700 - 16 GB RAM - 512 GB SSD - Tower - Windows 10 Pro 64-bit NVIDIA Quadro P620 2 GB Graphics - DVD-Writer - Serial ATA Controller - English Keyboard.',
    'imageUrl': 'https://m.media-amazon.com/images/I/81nHkldsNJL._AC_UL320_.jpg',
    'rating': 4.1,
    'shareLink': 'https://www.amazon.com/Dell-Precision-3000-3640-Workstation/dp/B08M96SMB5/ref=sr_1_17?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=17Y4X0Q1VVDP4JH1KN1V&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1614700019&rnid=16225007011&s=computers-intl-ship&sr=1-17',
    'likes': 44
  },
  {
    'id': 3.5,
    'productId': 'computers',
    'name': 'NVIDIA Jetson Xavier NX Developer Kit',
    'price': 399.0,
    'description': 'The NVIDIA Jetson Xavier NX developer kit includes a power-efficient, compact Jetson Xavier NX module for AI edge devices. It benefits from new cloud-native support and accelerates the NVIDIA software stack in as little as 10 W with more than 10X the performance of its widely adopted predecessor, Jetson TX2.',
    'imageUrl': 'https://m.media-amazon.com/images/I/61m739zmagL._AC_UL320_.jpg',
    'rating': 5,
    'shareLink': 'https://www.amazon.com/NVIDIA-Jetson-Xavier-Developer-812674024318/dp/B086874Q5R/ref=sr_1_3?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=17Y4X0Q1VVDP4JH1KN1V&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1614700019&rnid=16225007011&s=computers-intl-ship&sr=1-3',
    'likes': 50
  },
  {
    'id': 4.1,
    'productId': 'games',
    'name': 'Witcher 3: Wild Hunt',
    'price': 59.9,
    'description': 'Built for endless adventure, the massive open world of The Witcher sets new standards in terms of size, depth and complexity.',
    'imageUrl': 'https://m.media-amazon.com/images/I/91rLnlZhGzL._AC_UL320_.jpg',
    'rating': 5,
    'shareLink': 'https://www.amazon.com/Witcher-3-Wild-Hunt-Nintendo-Switch/dp/B07SH3D6HT/ref=sxin_9?ascsubtag=amzn1.osa.c9e9b8c6-7494-4540-98f5-cbbc58131e89.ATVPDKIKX0DER.en_US&creativeASIN=B07SH3D6HT&cv_ct_cx=video+games&cv_ct_id=amzn1.osa.c9e9b8c6-7494-4540-98f5-cbbc58131e89.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=video+games&linkCode=oas&pd_rd_i=B07SH3D6HT&pd_rd_r=e6e3a63b-1c58-48f5-a8a9-ecfc7140a59b&pd_rd_w=ZnjnX&pd_rd_wg=fhSQL&pf_rd_p=35b32c02-1b41-4e49-9b89-0297af2446e1&pf_rd_r=0BCQA9M6ZMMG5V3349AB&qid=1614700354&sr=1-2-64f3a41a-73ca-403a-923c-8152c45485fe&tag=gadgetreview-tca-20',
    'likes': 93
  },
  {
    'id': 4.2,
    'productId': 'games',
    'name': 'Mass Effect Legendary Edition',
    'price': 59.9,
    'description': 'One person is all that stands between humanity and the greatest threat it\'s ever faced. Relive the legend of Commander Shepard remastered and optimized for 4K Ultra HD.',
    'imageUrl': 'https://m.media-amazon.com/images/I/71IbXCVb4pL._AC_UY218_.jpg',
    'rating': 5,
    'shareLink': 'https://www.amazon.com/Mass-Effect-Legendary-PlayStation-4/dp/B08MXTDGN6/ref=sr_1_5?dchild=1&keywords=video+games&qid=1614700553&sr=8-5',
    'likes': 70
  },
  {
    'id': 4.3,
    'productId': 'games',
    'name': 'The Last of Us Remastered',
    'price': 17.9,
    'description': 'Winner of over 200 Game of the Year awards. Explore a brutal post-pandemic world, fully realized with the power of PlayStation 4 system.',
    'imageUrl': 'https://m.media-amazon.com/images/I/51fR72yjSFL._AC_UL320_.jpg',
    'rating': 5,
    'shareLink': 'https://www.amazon.com/Last-Us-Remastered-PlayStation-4/dp/B00JK00S0S/ref=sxin_9?ascsubtag=amzn1.osa.c9e9b8c6-7494-4540-98f5-cbbc58131e89.ATVPDKIKX0DER.en_US&creativeASIN=B00JK00S0S&cv_ct_cx=video+games&cv_ct_id=amzn1.osa.c9e9b8c6-7494-4540-98f5-cbbc58131e89.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=video+games&linkCode=oas&pd_rd_i=B00JK00S0S&pd_rd_r=11b7bb4d-6baa-4dd9-8d5a-b34b5a49dac4&pd_rd_w=0fQ5s&pd_rd_wg=FnaBE&pf_rd_p=35b32c02-1b41-4e49-9b89-0297af2446e1&pf_rd_r=BJT1WK7E96M1KS7KNTHT&qid=1614700553&sr=1-3-64f3a41a-73ca-403a-923c-8152c45485fe&tag=gadgetreview-tca-20',
    'likes': 85
  },
  {
    'id': 4.4,
    'productId': 'games',
    'name': 'Mario & Sonic at the Olympic Games Tokyo',
    'price': 44.9,
    'description': 'Compete in all-new Olympic sports-skateboarding, surfing, Sport climbing, and karate-and a variety of events including archery, gymnastics, judo, boxing, marathon, football, equestrian, track and field, and many more.',
    'imageUrl': 'https://m.media-amazon.com/images/I/814xQ2+2s8L._AC_UL320_.jpg',
    'rating': 4.4,
    'shareLink': 'https://www.amazon.com/Mario-Sonic-Olympic-Games-Tokyo-2020/dp/B07SXNKFGS/ref=sxin_9?ascsubtag=amzn1.osa.c9e9b8c6-7494-4540-98f5-cbbc58131e89.ATVPDKIKX0DER.en_US&creativeASIN=B07SXNKFGS&cv_ct_cx=video+games&cv_ct_id=amzn1.osa.c9e9b8c6-7494-4540-98f5-cbbc58131e89.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=video+games&linkCode=oas&pd_rd_i=B07SXNKFGS&pd_rd_r=11b7bb4d-6baa-4dd9-8d5a-b34b5a49dac4&pd_rd_w=0fQ5s&pd_rd_wg=FnaBE&pf_rd_p=35b32c02-1b41-4e49-9b89-0297af2446e1&pf_rd_r=BJT1WK7E96M1KS7KNTHT&qid=1614700553&sr=1-4-64f3a41a-73ca-403a-923c-8152c45485fe&tag=gadgetreview-tca-20',
    'likes': 33
  },
  {
    'id': 4.5,
    'productId': 'games',
    'name': 'Persona 5 Strikers',
    'price': 59.9,
    'description': 'A summer vacation with close friends takes a sudden turn as a distorted reality emerges; reveal the truth and redeem the hearts of those imprisoned at the center of the crisis.',
    'imageUrl': 'https://m.media-amazon.com/images/I/81aEa8zePHL._AC_UY218_.jpg',
    'rating': 4.5,
    'shareLink': 'https://www.amazon.com/Persona-5-Strikers-PlayStation-4/dp/B08Q6YYLN5/ref=sr_1_1_sspa?dchild=1&keywords=video+games&qid=1614700553&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQjFGWTBIV1pLNUdYJmVuY3J5cHRlZElkPUEwMzEwOTU3M0dZUEtLNTgwRTlRNSZlbmNyeXB0ZWRBZElkPUEwODUxMDU5M0xRS0xIQjdNQVFDVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
    'likes': 68
  }
]

import json

with open('products.json', 'w') as fout:
  json.dump(products, fout)

with open('products.json', 'r') as fin:
  my_json = json.load(fin)

print(my_json)