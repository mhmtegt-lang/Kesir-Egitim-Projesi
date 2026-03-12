import streamlit as st
import matplotlib.pyplot as plt

# Sayfa Yapılandırması
st.set_page_config(page_title="Kesir Eğitimi", layout="centered")

st.title("🍎 Kesirleri Sıralama Eğitimi")
st.markdown("### Paydaları Eşit Kesirleri Karşılaştırma")

# --- YAN PANEL (Kontrol Merkezi) ---
st.sidebar.header("⚙️ Ayarlar ve Kontroller")
payda = st.sidebar.number_input("Payda (Bütünün Parçası)", min_value=2, max_value=20, value=8)

# Pay sürgülerini yan panele aldık, ana ekranı temizledik
pay1 = st.sidebar.slider("1. Kesrin Payı", 0, payda, 3)
pay2 = st.sidebar.slider("2. Kesrin Payı", 0, payda, 5)

ogrenci_adi = st.sidebar.text_input("Öğrenci Adı", "Küçük Matematikçi")

# --- 1. AŞAMA: GÖRSELLEŞTİRME (KESİR ÇUBUKLARI) ---
st.header("📊 Görsel Karşılaştırma")
st.write(f"Merhaba **{ogrenci_adi}**, aşağıdaki çubukları boyalı alanlarına göre incele:")

# Grafik mimarisi
fig, ax = plt.subplots(figsize=(10, 3))

# Kesir 1 Çizimi
ax.barh(1, 1, color='#F0F0F0', edgecolor='black', linewidth=1)
ax.barh(1, pay1/payda, color='#FF6B6B', label=f"1. Kesir: {pay1}/{payda}")

# Kesir 2 Çizimi
ax.barh(0, 1, color='#F0F0F0', edgecolor='black', linewidth=1)
ax.barh(0, pay2/payda, color='#4ECDC4', label=f"2. Kesir: {pay2}/{payda}")

# Izgara çizgileri (Payda kadar bölme)
for x in [i/payda for i in range(payda + 1)]:
    ax.axvline(x, color='black', linestyle=':', alpha=0.5)

# Görsel Temizlik: Eksenleri ve sayıları kaldır
ax.set_xlim(0, 1)
ax.set_xticks([]) # Alttaki sayıları kaldırdık
ax.set_yticks([0, 1])
ax.set_yticklabels(["2. Kesir", "1. Kesir"])
ax.legend(loc="upper right")

st.pyplot(fig)

# --- 2. AŞAMA: SOYUT KURAL ---
st.header("📝 Matematiksel Sonuç")

# Karşılaştırma Mantığı
if pay1 > pay2:
    sembol = ">"
    durum = "BÜYÜKTÜR"
elif pay1 < pay2:
    sembol = "<"
    durum = "KÜÇÜKTÜR"
else:
    sembol = "="
    durum = "EŞİTTİR"

# Büyük ve net bir sonuç kutusu
st.success(f"### $\\frac{{{pay1}}}{{{payda}}}$ {sembol} $\\frac{{{pay2}}}{{{payda}}}$")
st.markdown(f"**Yorum:** Paydalar eşit olduğunda, payı büyük olan ({max(pay1, pay2)}) daha büyüktür.")
