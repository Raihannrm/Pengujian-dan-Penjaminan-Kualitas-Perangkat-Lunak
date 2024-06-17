from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

path_to_chromedriver = r'C:\Users\DELL INSPIRON\chromedriver-win32\chromedriver.exe'

service = Service(path_to_chromedriver)
options = Options()

driver = webdriver.Chrome(service=service, options=options)

def login_berhasil():
    try:
        driver.get("https://shopee.co.id")

        login_button = driver.find_element(By.CLASS_NAME, "navbar__link--account")
        login_button.click()
        time.sleep(2)

        email_field = driver.find_element(By.NAME, 'loginKey')
        password_field = driver.find_element(By.NAME, 'password')

        email_field.send_keys('mraihanmaulana8@gmail.com')
        password_field.send_keys('Raihannrm8')

        login_submit_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn--primary')]")
        login_submit_button.click()
        time.sleep(5)

        dashboard_element = driver.find_element(By.CLASS_NAME, "dashboard")
        assert dashboard_element.is_displayed(), "Login tidak berhasil. Modul Login - Skenario Berhasil"
        print("Skenario Berhasil: Login berhasil. Test case TC001 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

def login_gagal_password_salah():
    try:
        driver.get("https://shopee.co.id")

        login_button = driver.find_element(By.CLASS_NAME, "navbar__link--account")
        login_button.click()
        time.sleep(2)

        username_input = driver.find_element(By.NAME, "loginEmail")
        password_input = driver.find_element(By.NAME, "loginPassword")
        username_input.send_keys("mraihanmaulana@gmail.com")
        password_input.send_keys("12345678")

        login_submit_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn--primary')]")
        login_submit_button.click()
        time.sleep(3)

        error_message = driver.find_element(By.CLASS_NAME, "error-message")
        assert error_message.is_displayed(), "Pesan kesalahan tidak muncul. Modul Login - Skenario Password Salah"
        print("Skenario Berhasil: Login gagal (Password Salah). Test case TC002 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

def login_gagal_tidak_mengisi_isian():
    try:
        driver.get("https://shopee.co.id")

        login_button = driver.find_element(By.CLASS_NAME, "navbar__link--account")
        login_button.click()
        time.sleep(2)

        login_submit_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn--primary')]")
        login_submit_button.click()
        time.sleep(3)

        error_message = driver.find_element(By.CLASS_NAME, "error-message")
        assert error_message.is_displayed(), "Pesan kesalahan tidak muncul. Modul Login - Skenario Tidak Mengisi Isian"
        print("Skenario Berhasil: Login gagal (Tidak Mengisi Isian). Test case TC003 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

def pencarian_produk_berhasil():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")

        search_box = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "laptop" in driver.page_source, "Produk tidak ditemukan dalam hasil pencarian. Modul Pencarian Produk - Skenario Berhasil"
        print("Skenario Berhasil: Pencarian produk berhasil. Test case TC004 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def pencarian_produk_tidak_ditemukan():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")

        search_box = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_box.send_keys("xyzabc")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "Tidak ditemukan hasil untuk xyzabc" in driver.page_source, "Produk ditemukan dalam hasil pencarian. Modul Pencarian Produk - Skenario Tidak Ditemukan"
        print("Skenario Berhasil: Pencarian produk tidak ditemukan. Test case TC005 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def penyaringan_hasil_pencarian():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/search?keyword=sepatu")
        time.sleep(2)

        category_filter = driver.find_element(By.XPATH, "//div[contains(text(), 'Kategori')]")
        category_filter.click()
        time.sleep(2)

        assert "Filter Kategori: Sepatu" in driver.page_source, "Penyaringan hasil pencarian tidak berhasil. Test case Penyaringan Hasil Pencarian - Skenario Berhasil"
        print("Skenario Berhasil: Penyaringan hasil pencarian berhasil. Test case TC006 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def tambahkan_produk_ke_keranjang_berhasil():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")

        search_box = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        product_link = driver.find_element(By.CSS_SELECTOR, ".shopee-search-item-result__item:nth-child(1) .yQmmFK")
        product_link.click()
        time.sleep(3)

        add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn--primary")
        add_to_cart_button.click()
        time.sleep(3)

        assert "Berhasil ditambahkan ke keranjang" in driver.page_source, "Produk tidak berhasil ditambahkan ke keranjang. Modul Menambahkan Produk ke Keranjang - Skenario Berhasil"
        print("Skenario Berhasil: Menambahkan produk ke keranjang berhasil. Test case TC007 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def tambahkan_produk_ke_keranjang_gagal():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")

        search_box = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_box.send_keys("barangtidakada")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        try:
            add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn--primary")
            assert not add_to_cart_button.is_displayed(), "Tombol 'Tambah ke Keranjang' muncul untuk produk yang tidak tersedia. Modul Menambahkan Produk ke Keranjang - Skenario Gagal"
        except NoSuchElementException:
            print("Skenario Berhasil: Menambahkan produk ke keranjang gagal (Produk tidak tersedia). Test case TC008 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def hapus_produk_dari_keranjang_berhasil():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/keranjang")
        time.sleep(3)

        delete_button = driver.find_element(By.XPATH, "//button[contains(@class,'cart-remove-item__delete-btn')]")
        delete_button.click()
        time.sleep(3)

        assert "Keranjang belanja Anda kosong" in driver.page_source, "Produk tidak berhasil dihapus dari keranjang. Modul Menghapus Produk dari Keranjang - Skenario Berhasil"
        print("Skenario Berhasil: Menghapus produk dari keranjang berhasil. Test case TC009 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def hapus_produk_dari_keranjang_gagal():
    try:
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/keranjang")
        time.sleep(3)

        try:
            empty_message = driver.find_element(By.CLASS_NAME, "shopee-cart-page__cart-empty-text")
            assert empty_message.is_displayed(), "Pesan 'Keranjang belanja Anda kosong' tidak muncul. Modul Menghapus Produk dari Keranjang - Skenario Gagal"
        except NoSuchElementException:
            print("Skenario Gagal: Tidak ada produk di keranjang untuk dihapus. Test case TC010 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def hapus_produk_dari_keranjang_berhasil():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/keranjang")
        time.sleep(3) 

        delete_button = driver.find_element_by_xpath("//button[contains(@class,'cart-remove-item__delete-btn')]")
        delete_button.click()
        time.sleep(3) 
    
        assert "Keranjang belanja Anda kosong" in driver.page_source, "Produk tidak berhasil dihapus dari keranjang. Modul Menghapus Produk dari Keranjang - Skenario Berhasil"
        print("Skenario Berhasil: Menghapus produk dari keranjang berhasil. Test case TC009 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def hapus_produk_dari_keranjang_gagal_kosong():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/keranjang")
        time.sleep(3) 

        assert "Keranjang belanja Anda kosong" in driver.page_source, "Ada opsi untuk menghapus produk dari keranjang yang kosong. Modul Menghapus Produk dari Keranjang - Skenario Gagal"
        print("Skenario Berhasil: Menghapus produk dari keranjang gagal (Keranjang kosong). Test case TC010 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def tambah_metode_pembayaran():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")
        time.sleep(2) 
        
        account_menu = driver.find_element_by_class_name("navbar__link--account")
        account_menu.click()
        time.sleep(2) 

        payment_menu = driver.find_element_by_xpath("//a[contains(text(), 'Metode Pembayaran')]")
        payment_menu.click()
        time.sleep(2)  
        
        # Tambahkan metode pembayaran baru
        # Di sini bisa diimplementasikan integrasi dengan payment gateway atau e-wallet

        assert "Metode pembayaran berhasil ditambahkan" in driver.page_source, "Metode pembayaran tidak berhasil ditambahkan. Test case Menambah Metode Pembayaran - Skenario Berhasil"
        print("Skenario Berhasil: Menambah metode pembayaran berhasil. Test case TC011 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def hapus_metode_pembayaran():
    try:
        
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")
        time.sleep(2) 

        account_menu = driver.find_element_by_class_name("navbar__link--account")
        account_menu.click()
        time.sleep(2)
 
        payment_menu = driver.find_element_by_xpath("//a[contains(text(), 'Metode Pembayaran')]")
        payment_menu.click()
        time.sleep(2)  
        
        # Hapus salah satu metode pembayaran
        # Di sini bisa diimplementasikan integrasi dengan payment gateway atau e-wallet

        assert "Metode pembayaran berhasil dihapus" in driver.page_source, "Metode pembayaran tidak berhasil dihapus. Test case Menghapus Metode Pembayaran - Skenario Berhasil"
        print("Skenario Berhasil: Menghapus metode pembayaran berhasil. Test case TC012 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def lihat_diskon_promosi():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/promo")
        time.sleep(2) 

        assert "Diskon dan Promosi" in driver.title, "Halaman diskon atau promosi tidak ditampilkan dengan benar. Test case Melihat Diskon atau Promosi - Skenario Berhasil"
        print("Skenario Berhasil: Halaman diskon atau promosi ditampilkan dengan benar. Test case TC013 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def gunakan_kode_promo():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/sepatu-pria")
        time.sleep(2)

        add_to_cart_button = driver.find_element_by_xpath("//button[contains(text(), 'Beli Sekarang')]")
        add_to_cart_button.click()
        time.sleep(2)

        checkout_button = driver.find_element_by_xpath("//button[contains(text(), 'Checkout')]")
        checkout_button.click()
        time.sleep(2)  

        promo_code_field = driver.find_element_by_name("promo_code")
        promo_code_field.send_keys("PROMO123")

        apply_promo_button = driver.find_element_by_xpath("//button[contains(text(), 'Gunakan')]")
        apply_promo_button.click()
        time.sleep(2) 

        assert "Diskon berhasil diterapkan" in driver.page_source, "Diskon dari kode promo tidak berhasil diterapkan. Test case Menggunakan Kode Promo - Skenario Berhasil"
        print("Skenario Berhasil: Diskon dari kode promo berhasil diterapkan. Test case TC014 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def selesaikan_pembelian():
    try:
        
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/keranjang")
        time.sleep(2) 

        assert "Sepatu Pria" in driver.page_source, "Produk tidak ditemukan di keranjang. Test case Menyelesaikan Pembelian - Skenario Berhasil"
        

        checkout_button = driver.find_element_by_xpath("//button[contains(text(), 'Checkout')]")
        checkout_button.click()
        time.sleep(2) 

        address_field = driver.find_element_by_name("address")
        address_field.send_keys("Jl. A Yani km 7 Banjarmasin")

        payment_method = driver.find_element_by_xpath("//input[@name='payment_method' and @value='bank_transfer']")
        payment_method.click()

        pay_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Bayar Sekarang')]")
        pay_now_button.click()
        time.sleep(2) 

        assert "Pesanan Anda berhasil dibuat" in driver.page_source, "Proses pembelian tidak selesai dengan baik. Test case Menyelesaikan Pembelian - Skenario Berhasil"
        print("Skenario Berhasil: Proses pembelian selesai. Test case TC015 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def lihat_ulasan_produk():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/sepatu-pria")
        time.sleep(2)

        review_section = driver.find_element_by_xpath("//a[contains(text(), 'Ulasan')]")
        review_section.click()
        time.sleep(2) 

        assert "Ulasan untuk Sepatu Pria" in driver.title, "Ulasan produk tidak ditampilkan dengan benar. Test case Melihat Ulasan Produk - Skenario Berhasil"
        print("Skenario Berhasil: Ulasan produk ditampilkan dengan benar. Test case TC016 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def tulis_ulasan_produk():
    try:
        
        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/sepatu-pria")
        time.sleep(2) 
        
        write_review_button = driver.find_element_by_xpath("//button[contains(text(), 'Beri Ulasan')]")
        write_review_button.click()
        time.sleep(2) 
 
        review_textarea = driver.find_element_by_name("review")
        review_textarea.send_keys("Sepatunya sangat bagus sesuai dengan deskripsi")

        rating_stars = driver.find_element_by_xpath("//span[@class='star-rating-star' and @data-rating='5']")
        rating_stars.click()

        submit_button = driver.find_element_by_xpath("//button[contains(text(), 'Kirim')]")
        submit_button.click()
        time.sleep(2) 

        assert "Ulasan berhasil ditambahkan" in driver.page_source, "Ulasan tidak berhasil ditambahkan. Test case Menulis Ulasan Produk - Skenario Berhasil"
        print("Skenario Berhasil: Ulasan berhasil ditambahkan. Test case TC017 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)
        
def perubahan_informasi_akun():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")
        time.sleep(2) 

        account_menu = driver.find_element_by_class_name("navbar__link--account")
        account_menu.click()
        time.sleep(2)

        profile_menu = driver.find_element_by_xpath("//a[contains(text(), 'Informasi Akun')]")
        profile_menu.click()
        time.sleep(2)
        
        # Ubah informasi akun (misalnya alamat pengiriman)
        address_field = driver.find_element_by_id("address")
        address_field.clear()
        address_field.send_keys("Jl. Sepakat KOmplek Joko No. 13")

        save_button = driver.find_element_by_class_name("btn-save")
        save_button.click()
        time.sleep(2)

        assert "Informasi akun berhasil diperbarui" in driver.page_source, "Perubahan informasi akun tidak berhasil disimpan. Test case Perubahan Informasi Akun - Skenario Berhasil"
        print("Skenario Berhasil: Perubahan informasi akun berhasil disimpan. Test case TC018 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def ubah_kata_sandi():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/profile")
        time.sleep(2) 
        
        security_settings = driver.find_element_by_xpath("//a[contains(text(), 'Pengaturan Keamanan')]")
        security_settings.click()
        time.sleep(2) 
    
        old_password_field = driver.find_element_by_name("old_password")
        new_password_field = driver.find_element_by_name("new_password")
        confirm_password_field = driver.find_element_by_name("confirm_password")

        old_password_field.send_keys("Raihannrm8")
        new_password_field.send_keys("Raihanmm123")
        confirm_password_field.send_keys("Raihanmm123")

        confirm_button = driver.find_element_by_xpath("//button[contains(text(), 'Konfirmasi')]")
        confirm_button.click()
        time.sleep(2)  
        
        assert "Kata sandi berhasil diubah" in driver.page_source, "Kata sandi tidak berhasil diubah. Test case Mengubah Kata Sandi - Skenario Berhasil"
        print("Skenario Berhasil: Kata sandi berhasil diubah. Test case TC019 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def atur_preferensi_akun():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id/profile")
        time.sleep(2) 
    
        account_settings = driver.find_element_by_xpath("//a[contains(text(), 'Pengaturan Akun')]")
        account_settings.click()
        time.sleep(2)  
        
        # Ubah preferensi yang diinginkan 
        # Misalnya, ubah bahasa atau pengaturan notifikasi
        
        save_button = driver.find_element_by_xpath("//button[contains(text(), 'Simpan')]")
        save_button.click()
        time.sleep(2)

        assert "Preferensi akun berhasil disimpan" in driver.page_source, "Preferensi akun tidak berhasil disimpan. Test case Mengatur Preferensi Akun - Skenario Berhasil"
        print("Skenario Berhasil: Preferensi akun berhasil disimpan. Test case TC020 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2) 

def logout_berhasil():
    try:

        login_berhasil()
        time.sleep(3)
        driver.get("https://shopee.co.id")
        time.sleep(2)

        logout_button = driver.find_element_by_class_name("navbar__link--account")
        logout_button.click()
        time.sleep(2) 

        assert "Login" in driver.page_source, "Logout tidak berhasil. Modul Logout - Skenario Berhasil"
        print("Skenario Berhasil: Logout berhasil. Test case TC021 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)

def logout_gagal_belum_login():
    try:
        # Buka halaman utama tanpa login terlebih dahulu
        driver.get("https://shopee.co.id")
        time.sleep(2) 
        logout_button = driver.find_element_by_class_name("navbar__link--logout")
        assert not logout_button.is_displayed(), "Terdapat tombol logout padahal belum login. Modul Logout - Skenario Gagal"
        print("Skenario Berhasil: Logout gagal (Belum login). Test case TC022 passed.")

    except AssertionError as e:
        print(f"Gagal: {e}")

    finally:
        driver.get("https://shopee.co.id")
        time.sleep(2)


login_berhasil()
login_gagal_password_salah()
login_gagal_tidak_mengisi_isian()
pencarian_produk_berhasil()
pencarian_produk_tidak_ditemukan()
penyaringan_hasil_pencarian()
tambahkan_produk_ke_keranjang_berhasil()
tambahkan_produk_ke_keranjang_gagal()
hapus_produk_dari_keranjang_berhasil()
hapus_produk_dari_keranjang_gagal_kosong()
tambah_metode_pembayaran()
hapus_metode_pembayaran()
lihat_diskon_promosi()
gunakan_kode_promo()
selesaikan_pembelian()
lihat_ulasan_produk()
tulis_ulasan_produk()
perubahan_informasi_akun()
ubah_kata_sandi()
atur_preferensi_akun()
logout_berhasil()
logout_gagal_belum_login()

driver.quit()