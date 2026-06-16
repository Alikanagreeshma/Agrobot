/**
 * API Client for AgroBot Backend
 * Handles all communication with the Flask backend
 */

class APIClient {
    constructor(baseURL = 'http://localhost:10000') {
        this.baseURL = baseURL;
        this.timeout = 10000;
    }

    /**
     * Generic fetch wrapper with error handling
     */
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            timeout: this.timeout,
            ...options
        };

        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), this.timeout);

            const response = await fetch(url, {
                ...defaultOptions,
                signal: controller.signal
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                const error = await response.json().catch(() => ({}));
                throw new Error(error.message || `HTTP ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`API Error: ${endpoint}`, error);
            throw error;
        }
    }

    /**
     * Chat endpoint
     */
    async sendMessage(message, sessionId = 'default') {
        return this.request('/api/chat', {
            method: 'POST',
            body: JSON.stringify({
                message,
                session_id: sessionId
            })
        });
    }

    /**
     * Get chat session history
     */
    async getSession(sessionId) {
        return this.request(`/api/chat/session/${sessionId}`, {
            method: 'GET'
        });
    }

    /**
     * Clear chat session
     */
    async clearSession(sessionId) {
        return this.request(`/api/chat/session/${sessionId}`, {
            method: 'DELETE'
        });
    }

    /**
     * Get all chat sessions
     */
    async getAllSessions() {
        return this.request('/api/chat/sessions', {
            method: 'GET'
        });
    }

    /**
     * Agriculture endpoints
     */
    async getCrops() {
        return this.request('/api/agriculture/crops', {
            method: 'GET'
        });
    }

    async getCropRecommendation(cropName) {
        return this.request(`/api/agriculture/crops/${cropName}`, {
            method: 'GET'
        });
    }

    async getFertilizerRecommendations() {
        return this.request('/api/agriculture/fertilizer', {
            method: 'GET'
        });
    }

    async getIrrigationRecommendations() {
        return this.request('/api/agriculture/irrigation', {
            method: 'GET'
        });
    }

    async getSoilHealthTips() {
        return this.request('/api/agriculture/soil-health', {
            method: 'GET'
        });
    }

    async getPestManagementAdvice() {
        return this.request('/api/agriculture/pests', {
            method: 'GET'
        });
    }

    /**
     * Health check
     */
    async healthCheck() {
        return this.request('/health', {
            method: 'GET'
        });
    }
}

// Create global instance
const apiClient = new APIClient();
