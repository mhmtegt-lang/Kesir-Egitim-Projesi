import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Sayfa Yapılandırması - Mimari temizlik için
st.set_page_config(page_title="Kesir Eğitimi - CRA Modeli", layout="centered")

st.title("🍎 Kesirleri Sıralama Eğitimi")
st.markdown("### 5. Sınıf Müfredatına Uygun Somuttan Soyuta Öğrenme")

# --- YAN PANEL (Ayarlar) ---
st.sidebar.header("⚙️ Ders Ayarları")
# Payda (Bütünün kaç parçaya bölündüğü)
payda = st.sidebar.number_input("Bütün Kaç Parçadan Oluşsun? (Payda)", min_value=2, max_value=20, value=8)
ogrenci_adi = st.sidebar.text_input("Öğrenci Adı", "Küçük Matematikçi")

# --- 1. AŞAMA: SOMUT ---
st.header("1. Adım: Somut Deneyim (Lego Modeli)")
st.info(f"Merhaba {ogrenci_adi}! Elimizde {payda} parçalık bir Lego zemini var.")

col1, col2 = st.columns(2)
with col1:
    pay1 = st.slider("1. Kesrin Payı", 0, payda, 3)
with col2:
    pay2 = st.slider("2. Kesrin Payı", 0, payda, 5)

def draw_lego(pay, total, label):
    st.write(f"**{label} ({pay}/{total})**")
    full_blocks = "🟩" * pay
    empty_blocks = "⬜" * (total - pay)
    st.text(full_blocks + empty_blocks)

draw_lego(pay1, payda, "Senin Kulen")
draw_lego(pay2, payda, "Arkadaşının Kulesi")

# --- 2. AŞAMA: YARI-SOMUT (GÖRSEL) ---
st.header("2. Adım: Görselleştirme (Kesir Çubukları)")

# Grafik mimarisini oluştur
fig, ax = plt.subplots(figsize=(10, 3))

# 1. Kesir (Arka plan + Boyalı kısım)
ax.barh(1, 1, color='#F0F0F0', edgecolor='black', linewidth=1)
ax.barh(1, pay1/payda, color='#FF6B6B', label=f"Kesir 1: {pay1}/{payda}")

# 2. Kesir (Arka plan + Boyalı kısım)
ax.barh(0, 1, color='#F0F0F0', edgecolor='black', linewidth=1)
ax.barh(0, pay2/payda, color='#4ECDC4', label=f"Kesir 2: {pay2}/{payda}")

# Grid ve detaylar - Diskalkuli desteği için bölme çizgileri
for x in [i/payda for i in range(payda + 1)]:
    ax.axvline(x, color='black', linestyle=':', alpha=0.5)

# === DEĞİŞİKLİK BURADA BAŞLIYOR ===
# 1. X-ekseni sınırlarını bütünün tamamına (0-1 arası) ayarla
ax.set_xlim(0, 1)

# 2. X-ekseni üzerindeki sayısal etiketleri (ticks) tamamen kaldır!
# Bu satır, alttaki 0.0, 0.2, 0.4 vb. sayıları kaldırır.
ax.set_xticks([]) 
# === DEĞİŞİKLİK BURADA BİTİYOR ===

# Y-ekseni etiketleri (Kesir 1 / Kesir 2)
ax.set_yticks([0, 1])
ax.set_yticklabels(["Kesir 2", "Kesir 1"])
ax.legend(loc="upper right")
st.pyplot(fig)

# --- 3. AŞAMA: SOYUT ---
st.header("3. Adım: Soyut Kural (Matematik Sembolü)")

if pay1 > pay2:
    sembol = ">"
    mesaj = f"Çünkü {pay1} parça, {pay2} parçadan daha fazladır!"
elif pay1 < pay2:
    sembol = "<"
    mesaj = f"Çünkü {pay2} parça, {pay1} parçadan daha fazladır!"
else:
    sembol = "="
    mesaj = "İki kesir de birbirine eşittir."

# LaTeX formatında temiz çıktı
st.success(f"### Sonuç: $\\frac{{{pay1}}}{{{payda}}}$ {sembol} $\\frac{{{pay2}}}{{{payda}}}$")
st.write(mesaj)
