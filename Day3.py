
#password validator


import re
common_passwords = ["password123", "qwerty", "letmein", "dragonball", "welcome", "admin123"]
common_passwords_lower = [pwd.lower() for pwd in common_passwords]

while True:
    password = input("Input password: ")
    
    errors = []  # Collect all errors
    
    # Check for empty password
    if not password:
        print("❌ Password cannot be empty\n")
        continue
    
    # Check all conditions
    if len(password) < 8:
        errors.append("❌ Must be at least 8 characters")
    
    if not any(char.isupper() for char in password):
        errors.append("❌ Must contain at least one uppercase letter")
    
    if not any(char.isdigit() for char in password):
        errors.append("❌ Must contain at least one digit")
    
    if password.lower() in common_passwords_lower:
        errors.append("❌ Password is too common")
    
    if re.search(r'(.)\1{2,}', password):
        errors.append("❌ Password should not have repeated characters (3+ in a row)")
    
    # Calculate password strength (only if no errors)
    if not errors:
        strength = 0
        
        # Length scoring
        if len(password) >= 10:
            strength += 2
        elif len(password) >= 8:
            strength += 1
        
        # Special characters
        if any(not char.isalnum() for char in password):
            strength += 2
        
        # Mixed case
        if any(char.isupper() for char in password) and any(char.islower() for char in password):
            strength += 2
        
        # Contains digits
        if any(char.isdigit() for char in password):
            strength += 1
        
        # Determine strength level
        if strength <= 3:
            strength_level = "💛 Weak"
        elif strength <= 5:
            strength_level = "🧡 Medium"
        else:
            strength_level = "💚 Strong"
        
        print(f"✅ Password is valid! Strength: {strength_level} ({strength}/7 points)")
        break
    else:
        # Display all errors
        print("\n🔒 Password requirements not met:")
        for error in errors:
            print(f"  {error}")
        print()  # Blank line for readability