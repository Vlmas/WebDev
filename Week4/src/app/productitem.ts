export interface Product {
  id: number,
  name: string,
  price: number,
  description: string,
  imageUrl: string,
  rating: number,
  shareLink: string
}

export const images: string[] = [
  'https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNX/Jetson_Xavier_NX-Developer_Kit-Front_Top_Right.png',
  'https://images-na.ssl-images-amazon.com/images/I/618wPmm0hBL._AC_SL1500_.jpg',
  'https://images-na.ssl-images-amazon.com/images/I/41DV+Tq+4BL._SX346_BO1,204,203,200_.jpg',
  'https://m.media-amazon.com/images/I/81QnPIBbZML._AC_UY218_.jpg',
  'https://m.media-amazon.com/images/I/61AAq8ey6xL._AC_UY218_.jpg',
  'https://m.media-amazon.com/images/I/515J3bn6YdL._AC_UY218_.jpg',
  'https://m.media-amazon.com/images/I/71an9eiBxpL._AC_UY218_.jpg',
  'https://m.media-amazon.com/images/I/61Y+i9RK-VL._AC_UY218_.jpg',
  'https://m.media-amazon.com/images/I/51-6BAu2kbL._AC_UY218_.jpg',
  'https://m.media-amazon.com/images/I/81s2ELLTObL._AC_UY218_.jpg'
];

export const products: Product[] = [
  {
    id: 1, 
    name: 'NVIDIA Jetson Xavier NX Developer Kit', 
    price: 397.7, 
    description: 'The NVIDIA Jetson Xavier NX developer kit includes a power-efficient, compact Jetson Xavier NX module for AI edge devices.', 
    imageUrl: images[0],
    rating: 5.0,
    shareLink: 'https://www.amazon.com/NVIDIA-Jetson-Xavier-Developer-812674024318/dp/B086874Q5R/ref=sr_1_2?dchild=1&fst=as%3Aoff&pd_rd_r=c3455b75-5547-4b5d-89f5-b1dc3e727548&pd_rd_w=ifpUd&pd_rd_wg=IBVZZ&pf_rd_p=83ab1c34-7657-4d09-b72d-0a3e4b634b1d&pf_rd_r=65AHWSAMJHRB083VJGKP&qid=1602294815&rnid=16225007011&s=computers-intl-ship&sr=1-2'
  },
  {
    id: 2, 
    name: 'BOOX Note Air 10.3 ePaper', 
    price: 479.9, 
    description: 'Android 10, Front Light, G-Sensor, Digital Paper, E Ink Notepad.', 
    imageUrl: images[1],
    rating: 4.0,
    shareLink: 'https://www.amazon.com/BOOX-Android-G-Sensor-Digital-Notepad/dp/B08H83GCBT/ref=sr_1_1?dchild=1&fst=as%3Aoff&pd_rd_r=c3455b75-5547-4b5d-89f5-b1dc3e727548&pd_rd_w=ifpUd&pd_rd_wg=IBVZZ&pf_rd_p=83ab1c34-7657-4d09-b72d-0a3e4b634b1d&pf_rd_r=65AHWSAMJHRB083VJGKP&qid=1602294815&rnid=16225007011&s=computers-intl-ship&sr=1-1'
  },
  {
    id: 3, 
    name: 'iOS Programming: The Big Nerd Ranch Guide 7th Edition', 
    price: 19.3, 
    description: 'iOS Programming: The Big Nerd Ranch Guide leads you through the essential concepts, tools, and techniques for developing iOS applications.', 
    imageUrl: images[2],
    rating: 4.5,
    shareLink: 'https://www.amazon.com/iOS-Programming-Nerd-Ranch-Guide/dp/0135264022/ref=sr_1_3?dchild=1&keywords=ios&qid=1614171422&sr=8-3'
  },
  {
    id: 4, 
    name: 'MSI Gaming GeForce GTX 1660 Ti 192-bit', 
    price: 670.9, 
    description: 'Boost Clock: 1830 MHz; Core Clocks: 1770 MHz.', 
    imageUrl: images[3],
    rating: 5.0,
    shareLink: 'https://www.amazon.com/MSI-GeForce-GTX-1660-Ti/dp/B07N824KNV/ref=sr_1_1?dchild=1&keywords=gtx+1080&qid=1614171581&sr=8-1'
  },
  {
    id: 5, 
    name: 'Apple Watch Series 5', 
    price: 199.9, 
    description: 'Gold Aluminum Case with Pink Sand Sport Band.', 
    imageUrl: images[4],
    rating: 4.5,
    shareLink: 'https://www.amazon.com/Apple-Watch-GPS-40MM-Aluminum/dp/B083M6YZKT/ref=sr_1_7?crid=LESHANNLPTW8&dchild=1&keywords=apple+watch&qid=1614171738&sprefix=apple+wa%2Caps%2C388&sr=8-7'
  },
  {
    id: 6, 
    name: 'Apple iPhone XR 256 GB', 
    price: 490.9, 
    description: 'This pre-owned product is not Apple certified, but has been professionally inspected, tested and cleaned by Amazon-qualified suppliers.', 
    imageUrl: images[5],
    rating: 4.5,
    shareLink: 'https://www.amazon.com/Apple-iPhone-Virgin-Mobile-256GB/dp/B07T2SLHD4/ref=sr_1_8?dchild=1&keywords=iphone+Xr&qid=1614171885&sr=8-8'
  },
  {
    id: 7, 
    name: 'New Apple MacBook Pro with Apple M1 Chip', 
    price: 1299.0, 
    description: 'Apple-designed M1 chip for a giant leap in CPU, GPU, and machine learning performance', 
    imageUrl: images[6],
    rating: 4.5,
    shareLink: 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5N6RSS/ref=sr_1_1?dchild=1&keywords=macbook&qid=1614172060&sr=8-1'
  },
  {
    id: 8, 
    name: 'Zacro Gel Bike Seat Cover', 
    price: 23.9, 
    description: 'BS031 Extra Soft Gel Bicycle Seat - Bike Saddle Cushion with Water&Dust Resistant Cover (Black).', 
    imageUrl: images[7],
    rating: 4.5,
    shareLink: 'https://www.amazon.com/Zacro-Cover-BS031-Extra-Bicycle/dp/B01H71AZ36/ref=sr_1_1?dchild=1&keywords=bicycle&qid=1614172253&sr=8-1'
  },
  {
    id: 9, 
    name: 'Samsung Galaxy S10 Plus 512 GB', 
    price: 699.9, 
    description: '8GB RAM SM-G975F/DS Hybrid/Dual-SIM (GSM Only, No CDMA) Factory Unlocked 4G/LTE Smartphone - International Version No Warranty (Ceramic White).', 
    imageUrl: images[8],
    rating: 4.5,
    shareLink: 'https://www.amazon.com/Samsung-SM-G975F-Dual-SIM-Unlocked-Smartphone/dp/B07NWKP41X/ref=sr_1_1?dchild=1&keywords=samsung+s10&qid=1614172529&sr=8-1'
  },
  {
    id: 10, 
    name: 'Chivalry 2 PS5', 
    price: 39.9, 
    description: 'Unleash hell - own the field with a variety of heavy siege engines including ballistae, catapults, trebuchet, battering rams, mantlets, Spike traps, ladders and more', 
    imageUrl: images[9],
    rating: 5.0,
    shareLink: 'https://www.amazon.com/Chivalry-2-PS5-PlayStation-5/dp/B08X2JZ5LJ/ref=sr_1_1?dchild=1&keywords=ps5&qid=1614172652&sr=8-1'
  }
];