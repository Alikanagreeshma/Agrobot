"""
Agriculture service for handling farming recommendations and queries
"""


class AgricultureService:
    """Service for agriculture-related operations"""
    
    # Knowledge base for agriculture recommendations
    CROP_RECOMMENDATIONS = {
        "rice": {
            "season": "Kharif (June-November)",
            "water": "80-150 cm annually",
            "soil": "Clay or loamy soil",
            "temperature": "20-25°C",
            "fertilizer": "120 kg N, 60 kg P, 40 kg K per hectare"
        },
        "wheat": {
            "season": "Rabi (October-March)",
            "water": "45-60 cm annually",
            "soil": "Well-drained loamy soil",
            "temperature": "15-20°C",
            "fertilizer": "120 kg N, 60 kg P, 40 kg K per hectare"
        },
        "maize": {
            "season": "Kharif/Rabi",
            "water": "50-70 cm annually",
            "soil": "Well-drained fertile soil",
            "temperature": "21-27°C",
            "fertilizer": "150 kg N, 75 kg P, 40 kg K per hectare"
        },
        "cotton": {
            "season": "Kharif (June-November)",
            "water": "50-100 cm annually",
            "soil": "Black or loamy soil",
            "temperature": "21-30°C",
            "fertilizer": "120 kg N, 60 kg P, 30 kg K per hectare"
        }
    }
    
    FERTILIZER_RECOMMENDATIONS = {
        "npk_ratio": "The ratio depends on crop and soil conditions",
        "nitrogen": "Promotes vegetative growth and green color",
        "phosphorus": "Promotes root development and flowering",
        "potassium": "Enhances disease resistance and fruit quality",
        "organic": "Compost, farmyard manure, and vermicompost improve soil health"
    }
    
    IRRIGATION_RECOMMENDATIONS = {
        "drip": "Most efficient - saves 30-50% water, suitable for fruits and vegetables",
        "sprinkler": "Good for uniform distribution, suitable for grains and vegetables",
        "flood": "Traditional method, suitable for rice and wheat",
        "micro": "Fine control, suitable for vegetables and small plants",
        "frequency": "Depends on crop, soil, and weather conditions"
    }
    
    PEST_MANAGEMENT = {
        "integrated_pest_management": "Combine biological, cultural, and chemical methods",
        "crop_rotation": "Prevents pest buildup",
        "companion_planting": "Some plants repel pests naturally",
        "organic_pesticides": "Neem oil, soap solution, and botanical extracts"
    }
    
    SOIL_HEALTH = {
        "soil_testing": "Test soil pH, NPK, organic matter regularly",
        "composting": "Add organic matter to improve soil structure",
        "mulching": "Reduces water loss and maintains soil temperature",
        "crop_rotation": "Reduces pest buildup and improves soil health",
        "cover_crops": "Nitrogen fixation and organic matter addition"
    }
    
    def get_crop_recommendations(self, crop_name):
        """Get crop recommendations"""
        crop_name = crop_name.lower().strip()
        
        if crop_name in self.CROP_RECOMMENDATIONS:
            return {
                "status": "success",
                "crop": crop_name,
                "recommendations": self.CROP_RECOMMENDATIONS[crop_name]
            }
        
        return {
            "status": "partial",
            "message": f"Specific data for '{crop_name}' not available",
            "suggestion": "Please choose from: rice, wheat, maize, cotton",
            "available_crops": list(self.CROP_RECOMMENDATIONS.keys())
        }
    
    def get_fertilizer_guidance(self, query):
        """Get fertilizer guidance based on query"""
        query = query.lower()
        
        guidance = {
            "general": "Use balanced NPK fertilizers based on soil test results",
            "organic": self.FERTILIZER_RECOMMENDATIONS["organic"],
            "nitrogen": self.FERTILIZER_RECOMMENDATIONS["nitrogen"],
            "phosphorus": self.FERTILIZER_RECOMMENDATIONS["phosphorus"],
            "potassium": self.FERTILIZER_RECOMMENDATIONS["potassium"]
        }
        
        for key in guidance:
            if key in query:
                return {
                    "status": "success",
                    "topic": key,
                    "guidance": guidance[key]
                }
        
        return {
            "status": "success",
            "guidance": self.FERTILIZER_RECOMMENDATIONS
        }
    
    def get_irrigation_guidance(self, query):
        """Get irrigation guidance based on query"""
        query = query.lower()
        
        for method in self.IRRIGATION_RECOMMENDATIONS:
            if method.replace("_", " ") in query or method in query:
                return {
                    "status": "success",
                    "method": method,
                    "guidance": self.IRRIGATION_RECOMMENDATIONS[method]
                }
        
        return {
            "status": "success",
            "guidance": self.IRRIGATION_RECOMMENDATIONS
        }
    
    def get_pest_management_advice(self, query):
        """Get pest management advice"""
        query = query.lower()
        
        return {
            "status": "success",
            "topic": "Pest Management",
            "advice": self.PEST_MANAGEMENT
        }
    
    def get_soil_health_advice(self):
        """Get soil health advice"""
        return {
            "status": "success",
            "topic": "Soil Health",
            "advice": self.SOIL_HEALTH
        }
    
    def get_ai_response(self, user_query):
        """
        Generate AI response based on user query
        This is a basic implementation that routes to specific services
        Future: Replace with actual AI model integration (OpenAI, Gemini, etc.)
        """
        query_lower = user_query.lower()
        
        # Route to appropriate service based on keywords
        if any(keyword in query_lower for keyword in ["crop", "plant", "grow"]):
            crop_name = self._extract_crop_name(user_query)
            if crop_name:
                return self.get_crop_recommendations(crop_name)
            return {
                "status": "success",
                "response": "Please specify which crop you want to know about (rice, wheat, maize, cotton, etc.)"
            }
        
        elif any(keyword in query_lower for keyword in ["fertilizer", "nitrogen", "phosphorus", "potassium"]):
            return self.get_fertilizer_guidance(query_lower)
        
        elif any(keyword in query_lower for keyword in ["irrigation", "water", "drip", "sprinkler"]):
            return self.get_irrigation_guidance(query_lower)
        
        elif any(keyword in query_lower for keyword in ["pest", "disease", "insect", "worm"]):
            return self.get_pest_management_advice(query_lower)
        
        elif any(keyword in query_lower for keyword in ["soil", "health", "quality"]):
            return self.get_soil_health_advice()
        
        else:
            return {
                "status": "success",
                "response": "I can help with crop recommendations, fertilizer guidance, irrigation, pest management, and soil health. What would you like to know?"
            }
    
    def _extract_crop_name(self, text):
        """Extract crop name from text"""
        text_lower = text.lower()
        for crop in self.CROP_RECOMMENDATIONS.keys():
            if crop in text_lower:
                return crop
        return None
