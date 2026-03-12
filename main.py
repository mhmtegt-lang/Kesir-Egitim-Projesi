import streamlit as st
import matplotlib.pyplot as plt

# Sayfa Yapılandırması
st.set_page_config(page_title="Kesir Eğitimi", layout="centered")

st.title("🍎 Kesirleri Sıralama Eğitimi")
st.markdown("### Paydaları Eşit Kesirleri Karşılaştırma")

# --- YAN PANEL (Kontroller) ---
st.sidebar.header("⚙️ Ayarlar")
payda = st.sidebar.number_input("Payda (Toplam Parça)", min_value=2, max_value=20, value=8)
pay1 = st.sidebar.slider("1. Kesrin Payı", 0, payda, 3)
pay2 = st.sidebar.slider("2. Kesrin Payı", 0, payda, 5)
ogrenci_adi = st.sidebar.text_input("Öğrenci Adı", "Küçük Matematikçi")

# --- GÖRSELLEŞTİRME ---
st.header("📊 Görsel Karşılaştırma")
st.write(f"Merhaba **{ogrenci_adi}**, çubukları ve sağdaki kesir değerlerini incele:")

fig, ax = plt.subplots(figsize=(12, 3)) # Genişliği biraz artırdık ki yazılar sığsın

# Kesir 1 Çizimi
ax.barh(1, 1, color='#F0F0F0', edgecolor='black', linewidth=1)
ax.barh(1, pay1/payda, color='#FF6B6B')
# Sağ tarafa kesir metni ekleme
ax.text(1.02, 1, f"{pay1} / {payda}", va='center', ha='left', fontsize=14, fontweight='bold', color='#FF6B6B')

# Kesir 2 Çizimi
ax.barh(0, 1, color='#F0F0F0', edgecolor='black', linewidth=1)
ax.barh(0, pay2/payda, color='#4ECDC4')
# Sağ tarafa kesir metni ekleme
ax.text(1.02, 0, f"{pay2} / {payda}", va='center', ha='left', fontsize=14, fontweight='bold', color='#4ECDC4')

# Izgara çizgileri
for x in [i/payda for i in range(payda + 1)]:
    ax.axvline(x, color='black', linestyle=':', alpha=0.5)

# Görsel Temizlik
ax.set_xlim(0, 1.15) # Metinler için sağda %15'lik boşluk bıraktık
ax.set_xticks([])    # Alttaki sayıları gizledik
ax.set_yticks([0, 1])
ax.set_yticklabels(["2. Kesir", "1. Kesir"])

# Çerçeveyi sadeleştir
for spine in ax.spines.values():
    spine.set_visible(False)

st.pyplot(fig)

# --- MATEMATİKSEL SONUÇ ---
st.header("📝 Matematiksel Sonuç")

if pay1 > pay2:
    sembol = ">"
elif pay1 < pay2:
    sembol = "<"
else:
    sembol = "="

st.success(f"### $\\frac{{{pay1}}}{{{payda}}}$ {sembol} $\\frac{{{pay2}}}{{{payda}}}$")
st.write(f"**Mantık:** Paydalar eşit. {max(pay1, pay2)} parça, {min(pay1, pay2)} parçadan daha büyüktür.")
