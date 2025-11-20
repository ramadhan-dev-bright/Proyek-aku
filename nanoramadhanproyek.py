import random

print("hai salam kenal")
print("""perkenalkan aku proyek dari ramadhan, boleh
kutanya siapa namamu""")

nama = input("halo namaku kanjut: ")
print(f"halo {nama} salam kenal yaa")

input("iyaa (tekan enter untuk lanjut)")

umur = input("umur kamu berapa kalo boleh tau? ")

if umur.isdigit():
    umur = int(umur)
    if umur < 20:
        print("wahhh masih muda ternyata yaaa")
    else:
        print("wahh keren bangett kamunyaaa")
else:
    print(f"""hmmm {nama} tampaknya yang kamu masukan
bukan angka dehh coba lagi""")

kota = input("kamu asalnya dari kota mana? ")
print(f"wahh {kota} pasti banyak spot wisata disana ya")

hobi = input("oh iya hobi kamu apa kalo boleh tau? ")
if "mancing" in hobi.lower():
    print("wihh mancing! pasti orangnya penyabar")
elif "game" in hobi.lower():
    print("wahh gamer! pasti suka tantangan yaa kamu")
elif "nyanyi" in hobi.lower():
    print("wahhh nyanyi! suaranya bagus pasti tuhh")
else:
    print(f"wowww {hobi}! keren banget kamunyaaa")

random_list = [
        "kamu orangnya asik banget ihhh",
        "kamu aku suka jawabanmu tadi aowkaowk",
        "kok jadi seru ngobrolnya yaaa",
        f"{nama} seru banget ngobrol lama sama kamu",]

print("\n...membuat randok acak...")
print(random.choice(random_list))

rating = input("boleh kasih rating tentang proyek aku\n"
"dari 1-10?")

if rating.isdigit():
    rating = int(rating)
    if rating >= 8:
        print(f"wahh makasih {nama} makasih bangettt")
    elif rating >= 5:
        print("hmmmm boleh juga,aku akan terus belajarr")
else:
    print("""terima kasih masukanya,saya akan terus
belajar memperbaiki masalah ini""")

print("\n=====tebak tebakan jokes=====")
print("aku mau ngasih pertanyaaan")

tebakan = [{"hari hari apa yang tidak ada di tanggal? ":
"hariyanto xxiixi"},

{"ular,ular apa yang bikin sehat? ":
"ularaga xixixi"},

{"apa bahasa inggrinya monyet emas? ":
"golden monkey xixixix"},

{"apa bedanya fitnah sama fitnes? ":
"kalo fitnah kejam kalo fitnes kejim cixixi"}]


pilihan = random.choice(tebakan)
pertanyaan, jawaban = list(pilihan.items())[0]

print(pertanyaan)
jawaban_user = input("jawabanmu: ")

if jawaban_user.lower().strip() == jawaban.lower():
    print("wahhh jawabanya bener xixiixix")
else:
    print(f"""hampir benar aowkow, tapi
jawabannya {jawaban} aowmoakwkw lucu gak kayak aku kan""")
