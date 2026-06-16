/**
 * Voice Features for AgroBot
 * Handles speech recognition and synthesis
 */

class VoiceManager {
    constructor() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const SpeechSynthesisUtterance = window.SpeechSynthesisUtterance;
        
        this.recognitionAvailable = !!SpeechRecognition;
        this.synthesisAvailable = !!SpeechSynthesisUtterance;
        
        if (this.recognitionAvailable) {
            this.recognition = new SpeechRecognition();
            this.setupRecognition();
        }
        
        this.isListening = false;
        this.callbacks = {};
    }

    /**
     * Setup speech recognition
     */
    setupRecognition() {
        this.recognition.continuous = false;
        this.recognition.interimResults = true;
        this.recognition.language = 'en-US';

        this.recognition.onstart = () => {
            this.isListening = true;
            this.emit('listening', true);
        };

        this.recognition.onend = () => {
            this.isListening = false;
            this.emit('listening', false);
        };

        this.recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            this.emit('error', event.error);
        };

        this.recognition.onresult = (event) => {
            let interim = '';
            let final = '';

            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript;
                if (event.results[i].isFinal) {
                    final += transcript;
                } else {
                    interim += transcript;
                }
            }

            if (final) {
                this.emit('result', final);
            }
            if (interim) {
                this.emit('interim', interim);
            }
        };
    }

    /**
     * Start listening
     */
    startListening() {
        if (!this.recognitionAvailable) {
            console.warn('Speech recognition not available');
            return false;
        }

        if (this.isListening) {
            return false;
        }

        try {
            this.recognition.start();
            return true;
        } catch (error) {
            console.error('Error starting speech recognition:', error);
            return false;
        }
    }

    /**
     * Stop listening
     */
    stopListening() {
        if (!this.isListening) return;
        
        try {
            this.recognition.stop();
        } catch (error) {
            console.error('Error stopping speech recognition:', error);
        }
    }

    /**
     * Speak text
     */
    speak(text, language = 'en-US') {
        if (!this.synthesisAvailable) {
            console.warn('Speech synthesis not available');
            return false;
        }

        try {
            // Cancel any ongoing speech
            window.speechSynthesis.cancel();

            const utterance = new SpeechSynthesisUtterance(text);
            utterance.language = language;
            utterance.rate = 0.9;
            utterance.pitch = 1;
            utterance.volume = 1;

            utterance.onstart = () => this.emit('speaking', true);
            utterance.onend = () => this.emit('speaking', false);
            utterance.onerror = (error) => this.emit('error', error);

            window.speechSynthesis.speak(utterance);
            return true;
        } catch (error) {
            console.error('Error speaking:', error);
            return false;
        }
    }

    /**
     * Stop speaking
     */
    stopSpeaking() {
        try {
            window.speechSynthesis.cancel();
        } catch (error) {
            console.error('Error stopping speech:', error);
        }
    }

    /**
     * Set language for recognition
     */
    setLanguage(language) {
        if (this.recognitionAvailable) {
            this.recognition.language = language;
        }
    }

    /**
     * Event system
     */
    on(event, callback) {
        if (!this.callbacks[event]) {
            this.callbacks[event] = [];
        }
        this.callbacks[event].push(callback);
    }

    emit(event, data) {
        if (this.callbacks[event]) {
            this.callbacks[event].forEach(callback => callback(data));
        }
    }

    /**
     * Check feature availability
     */
    isRecognitionAvailable() {
        return this.recognitionAvailable;
    }

    isSynthesisAvailable() {
        return this.synthesisAvailable;
    }
}

// Create global instance
const voiceManager = new VoiceManager();
