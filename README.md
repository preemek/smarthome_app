# 🏠 Smart Home System - Django & MQTT

## **Opis projektu**
Smart Home System to aplikacja webowa oparta na Django, umożliwiająca zarządzanie inteligentnym domem za pomocą protokołu MQTT. System pozwala na sterowanie urządzeniami (np. światła, czujniki), monitorowanie danych z czujników, wizualizację danych oraz rozbudowę systemu o nowe funkcje. Projekt wspiera logowanie użytkowników, historię zdarzeń oraz konfigurację reguł automatyzacji.

---

## **🌟 Kluczowe funkcjonalności**

### **1. Podstawowe funkcjonalności**
- 🔒 **System logowania** – Każdy użytkownik posiada swój panel zarządzania.
- 💡 **Zdalne sterowanie urządzeniami** – Włączanie/wyłączanie światła lub innych urządzeń za pomocą tematów MQTT.
- 📜 **Historia zdarzeń** – Przegląd logów dotyczących akcji użytkowników i urządzeń.
- 🌐 **Integracja z MQTT** – Bezpośrednia komunikacja z ESP32 jako brokerem MQTT.
- 📋 **Lista urządzeń** – Możliwość zarządzania podłączonymi sensorami i aktuatorami.

### **2. Rozszerzone funkcjonalności**
- 📈 **Wizualizacja danych** – Tworzenie wykresów (np. zmiany temperatury, liczby interakcji) za pomocą bibliotek Matplotlib i Plotly.
- ➕ **Dodawanie nowych urządzeń** – Możliwość rozszerzenia systemu o nowe czujniki i aktuatory, dodawanie nowych tematów MQTT.
- ⚙️ **Panel ustawień** – Konfiguracja globalnych ustawień systemu, takich jak:
  - Adres brokera MQTT
  - Powiadomienia systemowe
  - Personalizacja nazw urządzeń
- 🤖 **Automatyzacja** – Tworzenie reguł, np. automatyczne włączanie światła o określonej godzinie.
- 📊 **Statystyki użytkownika** – Statystyki aktywności i interakcji w panelu użytkownika.

---

## **🛠️ Technologie**
- **Backend:** Python 3.10, Django 4.x
- **MQTT:** Broker ESP32 (lub inny, np. Mosquitto) za pomocą biblioteki `paho-mqtt`
- **Frontend:** HTML, CSS (Bootstrap)
- **Baza danych:** SQLite (domyślnie) lub PostgreSQL
- **Wizualizacja danych:** Matplotlib, Plotly
- **Protokół komunikacji:** MQTT

---

## **🚀 Jak zacząć pracę nad projektem?**

### **1. Klonowanie repozytorium**
Najpierw sklonuj projekt na swoje urządzenie:
```bash
git clone https://github.com/twoje_repo/smart-home-system.git
cd smart-home-system
