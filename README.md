# 🏠 Smart Home System - Django & MQTT

## **📖 Opis projektu**
Smart Home System to aplikacja webowa oparta na frameworku Django, umożliwiająca zarządzanie inteligentnym domem przy użyciu protokołu MQTT. System pozwala na zdalne sterowanie urządzeniami, wizualizację danych z sensorów oraz konfigurację reguł automatyzacji. Projekt wspiera logowanie użytkowników, współdzielenie urządzeń i jest łatwy do rozbudowy o nowe funkcjonalności.

---

## **🌟 Funkcjonalności**
- 🔒 **System logowania** – personalizowany dostęp dla użytkowników.
- 💡 **Sterowanie urządzeniami** – zdalne włączanie/wyłączanie światła i innych urządzeń.
- 📈 **Wykresy** – wizualizacja danych z czujników (np. temperatura, liczba interakcji).
- ⚙️ **Automatyzacja** – tworzenie reguł automatycznego sterowania urządzeniami.
- ➕ **Rozszerzalność** – możliwość dodawania nowych urządzeń i tematów MQTT.
- 📋 **Logi zdarzeń** – historia zdarzeń w systemie.
- 🌐 **Obsługa MQTT** – integracja z ESP32/ESP8266 lub innym brokerem MQTT (np. Mosquitto).

---

## **🛠️ Technologie**
- Backend: **Python 3.10**, **Django 4.x**
- Protokół komunikacji: **MQTT** (biblioteka `paho-mqtt`)
- Baza danych: SQLite (domyślnie) lub PostgreSQL
- Frontend: HTML, CSS (Bootstrap)
- Wizualizacja danych: **Matplotlib**, **Plotly**
- MQTT Broker: **ESP32** (możesz użyć Mosquitto jako alternatywy)

---

## **🚀 Jak zacząć pracę nad projektem?**

### **1. Klonowanie repozytorium**
Sklonuj repozytorium na swoje urządzenie:
```bash
git clone https://github.com/twoje_repo/smart-home-system.git
cd smart-home-system
