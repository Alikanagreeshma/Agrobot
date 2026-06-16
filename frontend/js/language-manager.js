/**
 * Multilingual Support for AgroBot
 */

class LanguageManager {
    constructor() {
        this.currentLanguage = localStorage.getItem('language') || 'en';
        this.translations = {
            'en': {
                'header': 'AgroBot - AI-Powered Smart Farming Assistant',
                'nav_home': 'Home',
                'nav_features': 'Features',
                'nav_about': 'About',
                'nav_contact': 'Contact',
                'nav_chat': 'Chat',
                'nav_dashboard': 'Dashboard',
                'hero_tagline': 'AI-Powered Smart Farming Assistant',
                'hero_description': 'Get instant farming advice powered by AI. Crop recommendations, fertilizer guidance, irrigation tips, and more.',
                'cta_get_started': 'Get Started',
                'cta_learn_more': 'Learn More',
                'chat_placeholder': 'Ask about crops, fertilizer, irrigation...',
                'clear_chat': 'Clear Chat',
                'new_chat': 'New Chat',
                'send': 'Send',
                'listen': 'Listen',
                'features': 'Features',
                'benefits': 'Benefits',
                'how_it_works': 'How It Works',
                'contact': 'Contact',
                'footer_about': 'About AgroBot',
                'footer_features': 'Features',
                'footer_support': 'Support',
                'footer_company': 'Company',
                'footer_legal': 'Legal',
                'copyright': '© 2024 AgroBot. All rights reserved.'
            },
            'hi': {
                'header': 'एग्रोबॉट - एआई-संचालित स्मार्ट कृषि सहायक',
                'nav_home': 'होम',
                'nav_features': 'फीचर्स',
                'nav_about': 'के बारे में',
                'nav_contact': 'संपर्क',
                'nav_chat': 'चैट',
                'nav_dashboard': 'डैशबोर्ड',
                'hero_tagline': 'एआई-संचालित स्मार्ट कृषि सहायक',
                'hero_description': 'एआई द्वारा संचालित तत्काल कृषि सलाह प्राप्त करें। फसल की सिफारिशें, उर्वरक मार्गदर्शन, सिंचाई सुझाव, और बहुत कुछ।',
                'cta_get_started': 'शुरुआत करें',
                'cta_learn_more': 'और जानें',
                'chat_placeholder': 'फसलें, उर्वरक, सिंचाई के बारे में पूछें...',
                'clear_chat': 'चैट साफ करें',
                'new_chat': 'नई चैट',
                'send': 'भेजें',
                'listen': 'सुनें',
                'features': 'फीचर्स',
                'benefits': 'लाभ',
                'how_it_works': 'यह कैसे काम करता है',
                'contact': 'संपर्क',
                'footer_about': 'एग्रोबॉट के बारे में',
                'footer_features': 'फीचर्स',
                'footer_support': 'सपोर्ट',
                'footer_company': 'कंपनी',
                'footer_legal': 'कानूनी',
                'copyright': '© 2024 एग्रोबॉट। सर्वाधिकार सुरक्षित।'
            },
            'te': {
                'header': 'ఆగ్రోబాట్ - AI-చేత నడిపిన స్మార్ట్ ఫార్మింగ్ సహాయక',
                'nav_home': 'హోమ్',
                'nav_features': 'ఫీచర్‌లు',
                'nav_about': 'గురించి',
                'nav_contact': 'సంపర్కం',
                'nav_chat': 'చాట్',
                'nav_dashboard': 'డ్యాష్‌బోర్డ్',
                'hero_tagline': 'AI-చేత నడిపిన స్మార్ట్ ఫార్మింగ్ సహాయక',
                'hero_description': 'AI ద్వారా ప్రేరితమైన తక్షణ సfarming సలహా పొందండి. పంట సిఫారసులు, ఖాద సూచన, నీటిపాచన చిట్కాలు మరియు మరెన్ని.',
                'cta_get_started': 'ప్రారంభించండి',
                'cta_learn_more': 'మరిన్ని తెలుసుకోండి',
                'chat_placeholder': 'పంటలు, ఖాద, నీటిపాచన గురించి అడగండి...',
                'clear_chat': 'చాట్‌ను సరిచేయండి',
                'new_chat': 'కొత్త చాట్',
                'send': 'పంపండి',
                'listen': 'వినండి',
                'features': 'ఫీచర్‌లు',
                'benefits': 'ప్రయోజనాలు',
                'how_it_works': 'ఇది ఎలా పనిచేస్తుంది',
                'contact': 'సంపర్కం',
                'footer_about': 'ఆగ్రోబాట్ గురించి',
                'footer_features': 'ఫీచర్‌లు',
                'footer_support': 'సపోర్ట్',
                'footer_company': 'కంపెనీ',
                'footer_legal': 'చట్టబద్ధ',
                'copyright': '© 2024 ఆగ్రోబాట్. అన్ని హక్కులు రక్షించబడ్డాయి.'
            }
        };
    }

    /**
     * Get translation for a key
     */
    t(key) {
        if (this.translations[this.currentLanguage] && this.translations[this.currentLanguage][key]) {
            return this.translations[this.currentLanguage][key];
        }
        if (this.translations['en'] && this.translations['en'][key]) {
            return this.translations['en'][key];
        }
        return key;
    }

    /**
     * Set current language
     */
    setLanguage(lang) {
        if (this.translations[lang]) {
            this.currentLanguage = lang;
            localStorage.setItem('language', lang);
            this.updatePageLanguage();
            return true;
        }
        return false;
    }

    /**
     * Get current language
     */
    getLanguage() {
        return this.currentLanguage;
    }

    /**
     * Get available languages
     */
    getAvailableLanguages() {
        return Object.keys(this.translations);
    }

    /**
     * Update page language
     */
    updatePageLanguage() {
        document.documentElement.lang = this.currentLanguage;
        
        // Update all data-i18n elements
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.dataset.i18n;
            element.textContent = this.t(key);
        });
        
        // Update all data-i18n-placeholder attributes
        document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
            const key = element.dataset.i18nPlaceholder;
            element.placeholder = this.t(key);
        });

        // Emit language change event
        window.dispatchEvent(new CustomEvent('languageChange', { detail: { lang: this.currentLanguage } }));
    }

    /**
     * Add new translations
     */
    addTranslations(lang, translations) {
        if (!this.translations[lang]) {
            this.translations[lang] = {};
        }
        this.translations[lang] = { ...this.translations[lang], ...translations };
    }
}

// Create global instance
const languageManager = new LanguageManager();
