---
name: thai-places
description: Lookup of Bangkok Post held forms for Thai districts, provinces and other Thai places under references.thai_places. Use only when a Thai district or an unfamiliar Thai place name needs its form checked during edit, check, photo or PR work.
---

# THAI PLACES

A lookup on top of `edit`. The listed form governs: each entry is a held form in its own right, and no entry sets a rule for another. Thai style conventions (Muang, sois, roads, postcodes, airports) are in `references.thai_conventions` in `edit`. Recent, consistent usage on the story tracker may be preferred to a listed form (SHIFT FILES). Consult the whole of the relevant branch.

```yaml
references:
  thai_places:

    note: >
      An unlisted Thai name stands as filed. Where it matches neither a held BKP
      form nor standard RTGS, query it without alteration.

    third_party_spellings: >
      Some institutions named after places spell their own names differently from BKP house
      style. Follow their official spelling for their name. Examples — Hatyai Hospital (BKP
      spells the town "Hat Yai"), Prince of Songkla University (not "Songkhla"), Sriracha
      Tiger Zoo (not "Sri Racha"), Minburi Prison (BKP spells the district "Min Buri"),
      Khlong Prem Prachakon (canal/prison area — an institutional name).

    bangkok_districts: [Bang Bon, Bang Kae, Bang Kapi, Bang Khen, Bang Kholaem, Bang Khunthian, Bang Na, Bang Phlat, Bang Rak, Bang Sue, Bangkok Noi, Bangkok Yai, Bung Kum, Chatuchak, Chom Thong, Din Daeng, Don Muang, Dusit, Huai Khwang, Kannayao, Klong Sam Wa, Klong San, Klong Toey, Laksi, Lat Krabang, Lat Phrao, Min Buri, Nong Chok, Nong Khaem, Pathumwan, Phasicharoen, Phaya Thai, Phra Khanong, Phra Nakhon, Pomprap Sattruphai, Prawet, Rat Burana, Ratchathewi, Sai Mai, Saphan Sung, Samphanthawong, Sathon, Suan Luang, Taling Chan, Thawi Watthana, Thon Buri, Thung Kru, Watthana, Wang Thonglang, Yannawa]

    provinces:
      Amnat Charoen: [Muang Amnat Charoen, Chanuman, Phana, Hua Thapan, Pathumrat Wongsa, Senangkhanikhom, Lue Amnat]
      Ang Thong: [Muang Ang Thong, Chaiyo, Pa Mok, Pho Thong, Samko, Sawaengha, Wiset Chai Chan]
      Ayutthaya: [Phra Nakhon Sri Ayutthaya, Ban Phraek, Bang Ban, Bang Pahan, Bang Pa-in, Bang Sa-ai, Bang Sai, Lat Bua Luang, Maha Rat, Nakhon Luang, Phachi, Phak Hai, Sena, Tha Rua, Uthai, Wang Noi]
      Bueng Kan: [Muang Bueng Kan, Bueng Khla, Bueng Khong Long, Pak Khat, Phon Charoen, Seka, Sri Wilai, So Phisai]
      Buri Ram: [Muang Buri Ram, Anapho, Ban Dan, Ban Kruat, Ban Mai Chai Pot, Chamni, Chalerm Phrakiat, Huai Rat, Khan Dong, Khu Muang, Krasang, Lahan Sai, Lam Plai Mat, Na Pho, Nang Rong, Non Suwan, Non Dindaeng, Nong Hong, Nong Ki, Pa Kham, Phlapphlachai, Phutthaisong, Prakhon Chai, Satuk]
      Chachoengsao: [Muang Chachoengsao, Ban Pho, Bang Khla, Bang Nam Prieo, Bang Pakong, Khlong Khuean, Phanom Sarakham, Plaeng Yao, Ratchasan, Sanam Chai Khet, Tha Takiab]
      Chai Nat: [Muang Chai Nat, Hankha, Manorom, Sankhaburi, Sapphaya, Wat Sing]
      Chaiyaphum: [Muang Chaiyaphum, Bamnet Narong, Ban Khwao, Ban Thaen, Chatturat, Kaeng Khro, Kaset Sombun, Khon San, Khon Sawan, Noen Sa-nga, Nong Bua Daeng, Nong Bua Rawe, Phu Khieo, Phakdi Chumphon, Sap Yai, Thep Sathit]
      Chanthaburi: [Muang Chanthaburi, Khaeng Hang Maew, Khao Kitchakut, Khlung, Laem Sing, Makham, Na Yai Am, Pong Nam Ron, Soi Dao, Tha Mai]
      Chiang Mai: [Muang Chiang Mai, Chai Prakan, Chiang Dao, Chom Thong, Doi Lo, Doi Saket, Doi Tao, Fang, Galyani Vadhana, Hang Dong, Hot, Mae Ai, Mae Chaem, Mae On, Mae Rim, Mae Taeng, Mae Wang, Omkoi, Phrao, Samoeng, San Kamphaeng, San Pa Tong, San Sai, Saraphi, Wiang Haeng]
      Chiang Rai: [Muang Chiang Rai, Chiang Khong, Chiang Saen, Doi Luang, Khun Tan, Mae Chan, Mae Fa Luang, Mae Lao, Mae Sai, Mae Suai, Pa Daet, Phan, Phaya Mengrai, Thoeng, Wiang Chai, Wiang Chiang Rung, Wiang Kaen, Wiang Pa Pao]
      Chon Buri: [Muang Chon Buri, Ban Bung, Bang Lamung, Bo Thong, Koh Chan, Koh Sichang, Nong Yai, Phan Thong, Phanat Nikhom, Sattahip, Sri Racha]
      Chumphon: [Muang Chumphon, Lamae, Lang Suan, Pathiu, Phato, Sawi, Tha Sae, Thung Tako]
      Kalasin: [Muang Kalasin, Don Chan, Huai Mek, Huai Phung, Kamalasai, Kham Muang, Khao Wong, Khong Chai Phatthana, Kuchinarai, Na Khu, Na Mon, Nong Kung Si, Rong Kham, Sahatsakhan, Sam Chai, Somdet, Tha Khantho, Yang Talat]
      Kamphaeng Phet: [Muang Kamphaeng Phet, Bueng Samakkhi, Kosamphinakhon, Khanu Woralaksaburi, Khlong Khlung, Khlong Lan, Lan Krabue, Pang Sila Thong, Phran Kratai, Sai Ngam, Sai Thong Watthana]
      Kanchanaburi: [Muang Kanchanaburi, Bo Phloi, Dan Makhamtia, Huay Krachao, Lao Khwan, Nong Prue, Phanom Thuan, Sai Yok, Sangkhla Buri, Sri Sawat, Tha Maka, Tha Muang, Thong Pha Phum]
      Khon Kaen: [Muang Khon Kaen, Ban Fang, Ban Hat, Ban Phai, Chonnabot, Chum Phae, Khao Suan Kwang, Khok Phochai, Kranuan, Mancha Khiri, Nam Phong, Non Sila, Nong Na Kham, Nong Rua, Nong Song Hong, Phon, Phra Yuen, Phu Pha Man, Phu Wiang, Puai Noi, Si Chomphu, Sam Soong, Ubon Ratana, Waeng Noi, Waeng Hai]
      Krabi: [Muang Krabi, Ao Luk, Khao Phanom, Khlong Thom, Koh Lanta, Lam Thap, Nua Khlong, Plai Phraya]
      Lampang: [Muang Lampang, Chae Hom, Hang Chat, Ko Kha, Mae Mo, Mae Phrik, Mae Tha, Muang Pan, Ngao, Soem Ngam, Sop Prap, Thoen, Wang Nua]
      Lamphun: [Muang Lamphun, Ban Hong, Ban Thi, Li, Mae Tha, Pa Sang, Thung Hua Chang, Wiang Nong Long]
      Loei: [Muang Loei, Chiang Khan, Dan Sai, Erawan, Na Duang, Na Haeo, Nong Hin, Pak Chom, Pha Khao, Phu Kradung, Phu Luang, Phu Rua, Tha Li, Wang Saphung]
      Lop Buri: [Muang Lop Buri, Ban Mi, Chai Badan, Khok Charoen, Khok Samrong, Lam Sonthi, Nong Muang, Phatthana Nikhom, Sa Bot, Tha Luang, Tha Wung]
      Mae Hong Son: [Muang Mae Hong Son, Khun Yuam, Mae La Noi, Mae Sariang, Pai, Pang Ma Pha, Sop Moei]
      Maha Sarakham: [Muang Maha Sarakham, Borabue, Chiang Yuen, Chuen Chom, Kae Dam, Kantharawichai, Kosum Phisai, Kut Rang, Na Chuak, Na Dun, Phayakkhaphum Phisai, Wapi Pathum, Yang Si Surat]
      Mukdahan: [Muang Mukdahan, Don Tan, Dong Luang, Khamcha-i, Nikhom Kham Soi, Nong Sung, Wan Yai]
      Nakhon Nayok: [Muang Nakhon Nayok, Ban Na, Ongkharak, Pak Phli]
      Nakhon Pathom: [Muang Nakhon Pathom, Bang Len, Buddha Monthon, Don Tum, Kamphaeng Saen, Nakhon Chaisi, Sam Phran]
      Nakhon Phanom: [Muang Nakhon Phanom, Ban Phaeng, Na Kae, Na Thom, Na Wa, Phon Sawan, Pla Pak, Renu Nakhon, Sri Songkhram, Tha Uthen, That Phanom, Wang Yang]
      Nakhon Ratchasima: [Muang Nakhon Ratchasima, Ban Luam, Bua Lai, Bua Yai, Chakkarat, Chalerm Phrakiat, Chok Chai, Chum Phuang, Dan Khun Thot, Huai Thalaeng, Kaeng Sanam Nang, Kham Sakae Saeng, Kham Thale So, Khon Buri, Khong, Lam Thamenchai, Muang Yang, Non Daeng, Non Sung, Non Thai, Nong Bunmak, Pak Chong, Pak Thong Chai, Phimai, Prathai, Pra Thong Kham, Sida, Sikhiu, Soeng Sang, Sung Noen, Thepharak, Wang Nam Khieo]
      Nakhon Sawan: [Muang Nakhon Sawan, Banphot Phisai, Chumsaeng, Chumtabong, Kao Lieo, Krok Phra, Lat Yao, Mae Poen, Mae Wong, Nong Bua, Phaisali, Phayuha Khiri, Tak Fa, Takhli, Tha Tako]
      Nakhon Si Thammarat: [Muang Nakhon Si Thammarat, Bang Khan, Chalerm Prakiat, Cha-uat, Chang Klang, Chawang, Chian Yai, Chulabhorn, Hua Sai, Khanom, Lan Saka, Na Bon, Nop Phi Tham, Pak Phanang, Phra Phom, Phipun, Phrommakhiri, Ron Phibun, Sichon, Tha Sala, Tham Phannara, Thung Song, Thung Yai]
      Nan: [Muang Nan, Ban Luang, Bo Klue, Chalerm Prakiat, Chiang Klang, Mae Charim, Na Muen, Na Noi, Pua, Phu Phiang, Santisuk, Song Khwer, Tha Wang Pha, Thung Chang, Wiang Sa]
      Narathiwat: [Muang Narathiwat, Bacho, Chanae, Cho Airong, Rangae, Rueso, Sri Sakhon, Sukhirin, Sungai Kolok, Sungai Padi, Tak Bai, Waeng, Yi-ngo]
      Nong Bua Lam Phu: [Muang Nong Bua Lam Phu, Na Klang, Na Wang, Nong Saeng, Sri Bun Ruang, Suwannakhuha]
      Nong Khai: [Muang Nong Khai, Fao Rai, Pho Tak, Phon Phisai, Ratana Wapi, Sa Khai, Sangkhom, Sri Chiang Mai, Tha Bo]
      Nonthaburi: [Muang Nonthaburi, Bang Bua Thong, Bang Kruai, Bang Yai, Pak Kret, Sai Noi]
      Pathum Thani: [Muang Pathum Thani, Khlong Luang, Lam Luk Ka, Lat Lum Kaeo, Nong Sua, Sam Khok, Thanyaburi]
      Pattani: [Muang Pattani, Kapho, Khok Pho, Mae Laen, Mai Kaen, Mayo, Nong Chik, Panare, Sai Buri, Tha Yang, Thung Yang Daeng, Yarang, Yaring]
      Phangnga: [Muang Phangnga, Kapong, Khura Buri, Koh Yao, Takua Pa, Takua Thung, Thai Muang, Thap Put]
      Phatthalung: [Muang Phatthalung, Bang Kaew, Khao Chaison, Khuan Khanun, Kong Ra, Pa Bon, Pa Phayom, Pak Phayun, Sri Banphot, Sri Nakharin, Tamot]
      Phayao: [Muang Phayao, Chiang Kham, Chiang Muan, Chun, Dok Kham Tai, Mae Chai, Phu Kham Yao, Phu Sang, Pong]
      Phetchabun: [Muang Phetchabun, Bung Sam Phan, Chon Daen, Khao Kho, Lom Kao, Lom Sak, Nam Nao, Nong Phai, Sri Thep, Wang Pong, Wichian Buri]
      Phetchaburi: [Muang Phetchaburi, Ban Laem, Ban Lat, Cha-am, Kang Krachan, Khao Yoi, Nong Ya Plong, Tha Yang]
      Phichit: [Muang Phichit, Bang Mun Nak, Bung Na Rang, Dong Charoen, Pho Prathap Chang, Pho Thale, Sam Ngam, Sak Lek, Taphan Hin, Thap Khlo, Wachira Banrami, Wang Sai Phun]
      Phitsanulok: [Muang Phitsanulok, Bang Krathum, Bang Rakam, Chat Trakan, Nakhon Thai, Noen Maprang, Phrom Phiram, Wang Thong, Wat Bot]
      Phrae: [Muang Phrae, Den Chai, Long, Nong Muang Khai, Rong Kwang, Song, Sung Men, Wang Chin]
      Phuket: [Muang Phuket, Kathu, Thalang]
      Prachin Buri: [Muang Prachin Buri, Ban Sang, Kabin Buri, Na Di, Prachantakham, Sri Maha Phot, Sri Mahosot (Khok Pip)]
      Prachuap Khiri Khan: [Muang Prachuap Khiri Khan, Bang Saphan, Bang Saphan Noi, Hua Hin, Kui Buri, Pran Buri, Sam Roi Yot, Thap Sakae]
      Ranong: [Muang Ranong, Kapoe, Kra Buri, La-un, Suk Samran]
      Ratchaburi: [Muang Ratchaburi, Ban Kha, Ban Pong, Bang Phae, Chom Bung, Damnoen Saduak, Pak Tho, Photharam, Suan Phung, Wat Phleng]
      Rayong: [Muang Rayong, Ban Chang, Ban Khai, Khao Chamao, Klaeng, Nikhom Phatthana, Pluak Daeng, Wang Chan]
      Roi Et: [Muang Roi Et, At Samat, Chang Han, Chaturaphak Phiman, Chiang Khwan, Kaset Wisai, Moeiwadi, Muang Suang, Nong He, Nong Phok, Pathum Rat, Phanom Phrai, Pho Chai, Phon Sai, Phon Thong, Selaphum, Sri Somdet, Suwannaphum, Thawatchaburi, Thung Khao Luang]
      Sa Kaeo: [Muang Sa Kaeo, Aranyaprathet, Khao Chakhan, Khlong Hat, Khok Sung, Ta Phraya, Watthana Nakhon, Wang Nam Yen, Wang Somboon]
      Sakon Nakhon: [Muang Sakon Nakhon, Akat Amnuai, Ban Muang, Charoen Sin, Kham Ta Kla, Khok Sri Suphan, Kusuman, Kut Bak, Nikhom Nam Un, Phang Khon, Phanna Nikhom, Phon Na Kaeo, Phu Phan, Sawang Daen Din, Song Dao, Tao Ngoi, Wanon Niwat, Waritchaphum]
      Samut Prakan: [Muang Samut Prakan, Bang Bo, Bang Chalong, Bang Pla, Bang Phli, Bang Poo, Bang Sao Thong, Phra Pradaeng, Phra Samut Chedi]
      Samut Sakhon: [Muang Samut Sakhon, Ban Phaeo, Krathum Baen]
      Samut Songkhram: [Muang Samut Songkhram, Amphawa, Bang Khonthi]
      Saraburi: [Muang Saraburi, Ban Mo, Chalerm Prakiat, Don Phut, Kaeng Khoi, Muak Lek, Nong Don, Nong Khae, Nong Saeng, Phra Phutthabat, Sao Hai, Wang Muang, Wihan Daeng]
      Satun: [Muang Satun, Khuan Don, Khuan Ka Long, Langu, Manang, Tha Phae, Thung Wa]
      Sing Buri: [Muang Sing Buri, Bang Rachan, In Buri, Khai Bang Rachan, Phrom Buri, Tha Chang]
      Songkhla: [Muang Songkhla, Bang Klam, Chana, Hat Yai, Khlong Hoi Khong, Khuan Niang, Krasae Sin, Na Mom, Na Thawi, Ranot, Rattaphum, Saba Yoi, Sadao, Sathing Phra, Singha Nakhon, Thepha]
      Sri Sa Ket: [Muang Sri Sa Ket, Bung Bun, Benchalak, Huai Thap Than, Kantharalak, Kanthararom, Khukhan, Khun Han, Muang Chan, Nam Kliang, Non Khun, Phayu, Pho Sri Suwan, Phrai Bung, Phu Sing, Prang Ku, Rasi Salai, Sila Lat, Sri Rattana, Uthumphon Phisai, Wang Hin, Yang Chum Noi]
      Sukhothai: [Muang Sukhothai, Ban Dan Lan Hoi, Khiri Mat, Kong Krailat, Sawankhalok, Sri Nakhon, Sri Samrong, Sri Satchanalai, Thung Saliam]
      Suphan Buri: [Muang Suphan Buri, Bang Pla Ma, Dan Chang, Doembang Nangbuat, Don Chedi, Nong Yasai, Sam Chuk, Sri Prachan, Song Phi Nong, U Thong]
      Surat Thani: [Muang Surat Thani, Ban Na Doem, Ban Na San, Ban Ta Khun, Chai Buri, Chaiya, Don Sak, Kanchanadit, Khian Sa, Khiri Ratthanikhom, Koh Phangan, Koh Samui, Phanom, Phrasaeng, Phunphin, Tha Chana, Tha Chang, Wiang Sa, Wipawadi]
      Surin: [Muang Surin, Buachet, Chom Phra, Chumphon Buri, Kap Choeng, Khewa Sinarin, Lamduan, Non Narai, Phanom Dong Rak, Prasat, Rattanaburi, Samrong Thap, Sangkha, Sanom, Sikhoraphum, Sri Narong, Tha Tum]
      Tak: [Muang Tak, Ban Tak, Mae Ramat, Mae Sot, Phop Phra, Sam Ngao, Tha Song Yang, Wang Chao, Umphang]
      Trang: [Muang Trang, Na Yong, Hat Samran, Huai Yot, Kantang, Palian, Ratsada, Sikao, Wang Wiset, Yan Ta Khao]
      Trat: [Muang Trat, Bo Rai, Khao Saming, Khlong Yai, Koh Chang, Koh Kut, Laem Ngop]
      Ubon Ratchathani: [Muang Ubon Ratchathani, Buntharik, Det Udom, Don Mot Daeng, Khemarat, Khong Chiam, Khuang Nai, Kut Khaopun, Lao Sue Kok, Muang Samsip, Na Chaluai, Na Tan, Na Yia, Nam Khun, Nam Yuen, Phibun Mangsahan, Pho Sai, Samrong, Sawang Wirawong, Sri Muang Mai, Sirinthorn, Tan Sum, Trakan Phuetphon, Thung Sri Udom, Warin Chamrap]
      Udon Thani: [Muang Udon Thani, Ban Dung, Ban Phue, Chaiwan, Ku Kaeo, Kumphawapi, Kut Chap, Nam Som, Na Yoong, Non Sa-at, Nong Han, Nong Sang, Nong Wua So, Phibun Rak, Phen, Prachak, Sang Khom, Sri That, Thung Fon, Wang Sam Mo]
      Uthai Thani: [Muang Uthai Thani, Ban Rai, Huai Khot, Lan Sak, Nong Chang, Nong Khayang, Sawang Arom, Thap Than]
      Uttaradit: [Muang Uttaradit, Ban Khok, Fak Tha, Laplae, Nam Pat, Phichai, Tha Pla, Thong Saen Khan, Tron]
      Yala: [Muang Yala, Bannang Sata, Betong, Kabang, Krong Pinang, Raman, Than To, Yaha]
      Yasothon: [Muang Yasothon, Kham Khuen Kaeo, Kho Wang, Kut Chum, Loeng Nok Tha, Maha Chana Chai, Pa Tiu, Thai Charoen, Sai Mun]
    other_places:
      Bangkok: [Bang Lamphu (area of Phra Nakhon; not a district), Khlong Thom Centre (market; not Klong Thom Centre)]
      Chon Buri: [Jomtien Beach (beach; not a district), Pattaya City (special administration; not a district), Khao Kheow Open Zoo (zoo)]
      Satun: [Ko Lipe (island; not a district)]
      Songkhla: [Dan Nok (town; not a district)]
      Regions: [Isan (not Isaan)]
```
