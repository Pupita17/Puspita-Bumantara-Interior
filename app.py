import streamlit as st
import urllib.parse

# 1. Konfigurasi Tampilan Utama Website
st.set_page_config(
    page_title="Puspita Bumantara Interior", 
    page_icon="🏠", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Nomor WhatsApp Bisnis (Format Internasional tanpa tanda +)
WA_NUMBER = "6282148985755"

# --- KUSTOMISASI DESAIN VISUAL (CSS) ---
st.markdown("""
    <style>
    /* Mengubah warna background utama dan teks */
    .main {
        background-color: #fcfbf7;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    h2, h3 {
        color: #34495e;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Mempercantik visual card informasi */
    .feature-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-top: 4px solid #d4af37; /* Aksen warna emas premium */
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGASI SIDEBAR ---
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.sidebar.image("assets/logo.png", width=260)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='text-align: center; color: #d4af37; margin-top: 10px;'>PUSPITA BUMANTARA</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; font-size: 13px; margin-top:-15px;'>Interior & Furniture Custom</p>", unsafe_allow_html=True)
st.sidebar.write("---")
page = st.sidebar.radio("Navigasi Halaman:", ["✨ Beranda Utama", "📂 Galeri Portofolio", "🧮 Simulasi Anggaran", "📞 Konsultasi & Survei"])
st.sidebar.write("---")
st.sidebar.caption("📍 Sengayam, Kotabaru, Kalsel")

# --- HALAMAN 1: BERANDA ---
if page == "✨ Beranda Utama":
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>✨ Puspita Bumantara Interior</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #a0aab2; margin-top:-15px;'>Jasa Desain Interior & Pembuatan Furnitur Kustom Premium</p>", unsafe_allow_html=True)
    st.write("")
    
    st.markdown("""
    <div style='background-color: #ffffff; color: #2c3e50; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); line-height: 1.8;'>
    Selamat datang di <b>Puspita Bumantara Interior</b>. Kami hadir sebagai solusi terbaik untuk mewujudkan interior hunian impian Anda di 
    <b>Sengayam, Kotabaru, Kalimantan Selatan</b>. Kami spesialis dalam merancang dan memproduksi 
    <b>Kitchen Set, Wardrobe (Lemari Pakaian), Backdrop TV, Kamar Set Modern</b>, hingga interior komersial ruko dan kantor. 
    Setiap detail furnitur kami kerjakan dengan material multiplex standar tinggi dan finishing HPL yang rapi, presisi, serta tahan lama.
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    # Nilai Jual (Keunggulan) dengan tampilan Kotak Mewah
    st.markdown("### 🛠️ Standar Layanan Unggulan Kami")
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("""
        <div class="feature-card">
            <h4 style="color: #2c3e50;">📐 Gratis Survei & Ukur</h4>
            <p style='font-size: 14px; color: #4a5568;'>Tim kami siap datang langsung ke lokasi Anda di wilayah Sengayam dan sekitarnya untuk melakukan pengukuran akurat tanpa dipungut biaya.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class="feature-card">
            <h4 style="color: #2c3e50;">⚒️ Material Berkualitas</h4>
            <p style='font-size: 14px; color: #4a5568;'>Menggunakan bahan dasar blokmin/multiplex pilihan (bukan serbuk kayu) dikombinasikan dengan engsel slow-motion & rel laci double track.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_c:
        st.markdown("""
        <div class="feature-card">
            <h4 style="color: #2c3e50;">💰 Budget Transparan</h4>
            <p style='font-size: 14px; color: #4a5568;'>Estimasi biaya dihitung secara transparan berdasarkan volume riil dengan standar harga bengkel produksi langsung Rp 2.000.000,- per meter lari.</p>
        </div>
        """, unsafe_allow_html=True)

# --- HALAMAN 2: GALERI PORTOFOLIO ---
elif page == "📂 Galeri Portofolio":
    st.title("📂 Portofolio Proyek Kustom")
    st.write("Koleksi desain interior eksklusif untuk inspirasi keindahan tata ruang Anda:")
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/kitchen.jpg", width="stretch") 
        st.markdown("<h4 style='margin-top:10px;'>1. Premium Kitchen Set Minimalis</h4>", unsafe_allow_html=True)
        st.caption("Konsep dapur bersih, fungsional, memaksimalkan ruang penyimpanan dengan kompartemen kustom.")
        
    with col2:
        st.image("assets/kamar.jpg", width="stretch") 
        st.markdown("<h4 style='margin-top:10px;'>2. Kamar Tidur Utama Kontemporer</h4>", unsafe_allow_html=True)
        st.caption("Pencahayaan warm light tersembunyi dikombinasikan dengan backdrop dipan minimalis untuk kenyamanan penuh.")

# --- HALAMAN 3: FITUR KALKULATOR BIAYA ---
elif page == "🧮 Simulasi Anggaran":
    st.title("🧮 Kalkulator Estimasi Anggaran")
    st.write("Simulasikan rencana biaya pembuatan furnitur Anda dengan standar harga Rp 2.000.000 / meter lari.")
    st.write("")
    
    with st.container(border=True):
        jenis_layanan = st.selectbox("Pilih Jenis Furnitur Kustom:", ["Kitchen Set (Atas/Bawah)", "Lemari Pakaian / Wardrobe", "Backdrop TV Modern", "Partisi Ruangan Dua Muka"])
        panjang = st.number_input("Perkiraan panjang furnitur yang Anda inginkan (dalam satuan meter):", min_value=1.0, value=2.0, step=0.5)
        
        HARGA_PER_METER = 2000000
        total_biaya = HARGA_PER_METER * panjang
        
        st.write("---")
        st.markdown(f"##### Kisaran Estimasi Total Biaya:")
        st.markdown(f"<h2 style='color: #27ae60;'>Rp {total_biaya:,.0f}</h2>", unsafe_allow_html=True)
        st.caption(f"Rumus hitung: {panjang} meter × Rp {HARGA_PER_METER:,.0f} (Belum termasuk aksesoris kustom tambahan seperti top table marmer/granit jika ada).")

# --- HALAMAN 4: HUBUNGI KAMI ---
elif page == "📞 Konsultasi & Survei":
    st.title("📞 Jadwalkan Konsultasi & Survei Lokasi")
    st.write("Silakan isi data di bawah ini untuk mengirimkan detail proyek langsung ke WhatsApp kami.")
    st.write("")
    
    with st.form("form_premium_puspita"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nama = st.text_input("Nama Lengkap")
            no_hp = st.text_input("Nomor Kontak / WhatsApp")
        with col_f2:
            alamat = st.text_input("Alamat Lengkap / Lokasi Proyek", value="Sengayam, Kotabaru")
            kebutuhan = st.selectbox("Rencana Pekerjaan Interior:", ["Pembuatan Kitchen Set", "Kamar Set Lengkap", "Backdrop TV & Ruang Keluarga", "Renovasi Rumah Total", "Lainnya"])
            
        catatan = st.text_area("Detail Tambahan (Contoh: Warna dominan putih, pakai cermin, atau ukuran ruangan)")
        st.write("")
        
        tombol_kirim = st.form_submit_button("Generate Formulir WhatsApp 💬")
        
        if tombol_kirim:
            if nama and no_hp:
                pesan_wa = f"Halo Puspita Bumantara Interior, saya *{nama}* ingin berkonsultasi mengenai proyek interior.\n\n📍 *Lokasi:* {alamat}\n🛠️ *Kebutuhan:* {kebutuhan}\n📝 *Catatan:* {catatan}"
                pesan_encoded = urllib.parse.quote(pesan_wa)
                link_whatsapp = f"https://whatsapp.com{WA_NUMBER}&text={pesan_encoded}"
                
                st.success("✅ Data formulir berhasil dibuat! Silakan klik tombol di bawah ini.")
                
                # METODE ANTI-BLOKIR MUTLAK: Menggunakan target='_self' agar langsung redirect di tab yang sama tanpa memicu pop-up blocker browser
                tombol_html = f"""
                <a href="{link_whatsapp}" target="_self" style="
                    display: block; 
                    width: 100%; 
                    padding: 14px; 
                    background-color: #25D366; 
                    color: white; 
                    text-align: center; 
                    text-decoration: none; 
                    font-size: 16px; 
                    border-radius: 6px; 
                    font-weight: bold; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    margin-top: 10px;
                ">Buka Obrolan WhatsApp Resmi Puspita Bumantara 💬</a>
                """
                st.markdown(tombol_html, unsafe_allow_html=True)
            else:
                st.error("⚠️ Nama Lengkap dan Nomor WhatsApp wajib diisi agar tim kami dapat merespons Anda.")
