import pywhatkit
import schedule
import time
import logging
from datetime import datetime, timedelta
import webbrowser
import pyautogui
import sys
import os

# Configure logging to handle Unicode properly
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('whatsapp_scheduler.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

class WhatsAppScheduler:
    def __init__(self):
        self.contacts = []
        self.setup_directories()
    
    def setup_directories(self):
        """Create necessary directories"""
        os.makedirs('logs', exist_ok=True)
        os.makedirs('contacts', exist_ok=True)
    
    def add_contact(self, phone_number, name=""):
        """Add WhatsApp contact with validation"""
        # Clean phone number
        phone_number = self.clean_phone_number(phone_number)
        
        if not self.validate_phone_number(phone_number):
            logging.error(f"Invalid phone number: {phone_number}")
            return False
        
        self.contacts.append({"phone": phone_number, "name": name})
        logging.info(f"Contact added: {name} ({phone_number})")
        return True
    
    def clean_phone_number(self, phone_number):
        """Clean and format phone number - FIXED VERSION"""
        # Store original to check if it already has +
        original_has_plus = phone_number.startswith('+')
        
        # Remove spaces, dashes, parentheses but KEEP the + if present
        if original_has_plus:
            # Keep the + and clean the rest
            digits = ''.join(filter(str.isdigit, phone_number[1:]))
            cleaned = '+' + digits
        else:
            # No +, clean all digits
            digits = ''.join(filter(str.isdigit, phone_number))
            
            # Check if it's a Ghana number (starts with 233)
            if digits.startswith('233') and len(digits) > 3:
                # It's already a Ghana number, add +
                cleaned = '+' + digits
            elif len(digits) == 9:
                # 9-digit Ghana number without country code
                cleaned = '+233' + digits
            else:
                # For other numbers, return as is (will fail validation)
                cleaned = '+' + digits
        
        return cleaned
    
    def validate_phone_number(self, phone_number):
        """Validate phone number format"""
        if not phone_number.startswith('+'):
            return False
        
        # Remove + and check if it's all digits
        digits = phone_number[1:]
        if not digits.isdigit():
            return False
        
        # Check Ghana number format (+233 followed by 9 digits)
        if phone_number.startswith('+233'):
            if len(digits) != 12:  # 233 + 9 digits = 12 total
                return False
        
        return True
    
    def save_contacts_to_file(self, filename="contacts/contacts_list.txt"):
        """Save contacts to a file for persistence"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for contact in self.contacts:
                    f.write(f"{contact['phone']},{contact['name']}\n")
            logging.info(f"Contacts saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to save contacts: {e}")
    
    def load_contacts_from_file(self, filename="contacts/contacts_list.txt"):
        """Load contacts from file"""
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            parts = line.split(',')
                            if len(parts) >= 2:
                                self.add_contact(parts[0], parts[1])
                logging.info(f"Contacts loaded from {filename}")
        except Exception as e:
            logging.error(f"Failed to load contacts: {e}")
    
    def send_whatsapp_message_direct(self, phone_number, message):
        """Alternative method using direct browser automation"""
        try:
            # Format WhatsApp URL
            import urllib.parse
            encoded_message = urllib.parse.quote(message)
            url = f"https://web.whatsapp.com/send?phone={phone_number[1:]}&text={encoded_message}"
            
            # Open in browser
            webbrowser.open(url)
            time.sleep(10)  # Wait for page to load
            
            # Press Enter to send
            pyautogui.press('enter')
            time.sleep(2)
            
            # Close tab
            pyautogui.hotkey('ctrl', 'w')
            
            return True
        except Exception as e:
            logging.error(f"Direct method failed: {e}")
            return False
    
    def send_whatsapp_message(self, message, use_direct_method=False):
        """Send WhatsApp message to all contacts with retry logic"""
        success_count = 0
        
        if not self.contacts:
            logging.error("No contacts to send messages to")
            return 0
        
        for contact in self.contacts:
            max_retries = 2
            for attempt in range(max_retries):
                try:
                    logging.info(f"Attempting to send to {contact['name']} ({contact['phone']}) - Attempt {attempt + 1}")
                    
                    if use_direct_method:
                        # Use direct browser method
                        if self.send_whatsapp_message_direct(contact['phone'], message):
                            success_count += 1
                            break
                    else:
                        # Use pywhatkit method
                        now = datetime.now()
                        send_time = now + timedelta(minutes=2)
                        
                        pywhatkit.sendwhatmsg(
                            contact['phone'],
                            message,
                            send_time.hour,
                            send_time.minute,
                            wait_time=20,  # Increased wait time
                            tab_close=True,
                            close_time=3
                        )
                        
                        success_count += 1
                        break
                        
                except Exception as e:
                    error_msg = str(e)
                    logging.warning(f"Attempt {attempt + 1} failed for {contact['phone']}: {error_msg}")
                    
                    if attempt < max_retries - 1:
                        logging.info(f"Retrying in 30 seconds...")
                        time.sleep(30)
                    else:
                        logging.error(f"Failed to send to {contact['phone']} after {max_retries} attempts")
                        
                        # Try direct method as fallback
                        if not use_direct_method:
                            logging.info("Trying direct method as fallback...")
                            if self.send_whatsapp_message_direct(contact['phone'], message):
                                success_count += 1
                
                # Wait between messages to avoid rate limiting
                time.sleep(15)
        
        logging.info(f"WhatsApp sending completed: {success_count}/{len(self.contacts)} successful")
        return success_count
    
    def schedule_hourly_messages(self, message_template, use_direct_method=False):
        """Schedule WhatsApp messages every hour"""
        def job():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            customized_message = f"{message_template}\n\nSent at: {current_time}"
            
            logging.info(f"Running scheduled job at {current_time}")
            self.send_whatsapp_message(customized_message, use_direct_method)
        
        # Schedule every hour
        schedule.every().hour.do(job)
        logging.info("Hourly WhatsApp scheduler started")
        
        # Run immediately once
        logging.info("Sending initial message...")
        job()
        
        # Keep running
        logging.info("Scheduler is running. Press Ctrl+C to stop.")
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Scheduler stopped by user")
    
    def send_test_message(self, phone_number, message="Test message from WhatsApp Scheduler"):
        """Send a test message to verify setup"""
        try:
            logging.info(f"Sending test message to {phone_number}")
            
            now = datetime.now()
            send_time = now + timedelta(minutes=2)
            
            pywhatkit.sendwhatmsg(
                phone_number,
                message,
                send_time.hour,
                send_time.minute,
                wait_time=15,
                tab_close=True
            )
            
            logging.info("Test message sent successfully!")
            return True
            
        except Exception as e:
            logging.error(f"Test message failed: {e}")
            return False

def main():
    """Main function to run the scheduler"""
    print("\n" + "="*50)
    print("WHATSAPP HOURLY MESSAGE SCHEDULER")
    print("="*50)
    print("GHANA NUMBER SUPPORT")
    print("="*50)
    
    # Create scheduler instance
    scheduler = WhatsAppScheduler()
    
    # Load existing contacts from file (if any)
    scheduler.load_contacts_from_file()
    
    # Show current contacts
    if scheduler.contacts:
        print(f"\nLoaded {len(scheduler.contacts)} contacts from file:")
        for contact in scheduler.contacts:
            print(f"  - {contact['name']}: {contact['phone']}")
    else:
        print("\nNo contacts found. Let's add some.")
    
    # Contact management
    while True:
        print("\nCONTACT MANAGEMENT:")
        print("1. Add new contact")
        print("2. Start messaging with current contacts")
        print("3. Show current contacts")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == "1":
            print("\nGHANA NUMBER FORMATS:")
            print("  - +233532661209    (Full international)")
            print("  - 0532661209       (Local with 0)")
            print("  - 532661209        (Local without 0)")
            
            phone = input("\nEnter phone number: ").strip()
            if phone:
                name = input("Enter contact name (optional): ").strip()
                original_phone = phone  # Store for display
                if scheduler.add_contact(phone, name):
                    scheduler.save_contacts_to_file()
                    # Show what it was converted to
                    final_phone = scheduler.contacts[-1]['phone']
                    print(f"✅ Added: {name}")
                    print(f"   Input: {original_phone}")
                    print(f"   Final: {final_phone}")
                else:
                    print("❌ Failed to add contact. Please check the number format.")
        
        elif choice == "2":
            if not scheduler.contacts:
                print("No contacts added. Please add contacts first.")
                continue
            break
        
        elif choice == "3":
            if scheduler.contacts:
                print(f"\nCurrent contacts ({len(scheduler.contacts)}):")
                for i, contact in enumerate(scheduler.contacts, 1):
                    print(f"  {i}. {contact['name']} - {contact['phone']}")
            else:
                print("No contacts added yet.")
        
        elif choice == "4":
            print("Goodbye!")
            return
        
        else:
            print("Invalid choice. Please try again.")
    
    # Message setup
    print("\nMESSAGE SETUP:")
    default_message = """Hello!

This is your automated hourly update from our system.

Everything is running smoothly!

Have a great day!"""
    
    print(f"Default message:\n{default_message}")
    use_default = input("\nUse this message? (y/n): ").strip().lower()
    
    if use_default == 'y':
        message_template = default_message
    else:
        message_template = input("Enter your custom message: ").strip()
        if not message_template:
            message_template = default_message
    
    # Sending method
    print("\nSELECT SENDING METHOD:")
    print("1. Standard method (Recommended)")
    print("2. Direct browser method (Use if standard fails)")
    method_choice = input("Enter 1 or 2: ").strip()
    
    use_direct_method = (method_choice == "2")
    
    # Start scheduler
    print(f"\nStarting scheduler with {len(scheduler.contacts)} contacts...")
    print("IMPORTANT: Make sure WhatsApp Web is OPEN in your browser!")
    print("Messages will be sent every hour")
    print("Press Ctrl+C to stop the scheduler\n")
    
    try:
        scheduler.schedule_hourly_messages(message_template, use_direct_method)
    except KeyboardInterrupt:
        print("\nScheduler stopped by user. Goodbye!")
    except Exception as e:
        logging.error(f"Scheduler crashed: {e}")
        print("Tip: Try running with direct method (option 2)")

if __name__ == "__main__":
    main()