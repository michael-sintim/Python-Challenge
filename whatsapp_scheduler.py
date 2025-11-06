import pywhatkit
import time
import logging
from datetime import datetime
import webbrowser
import pyautogui
import sys
import os
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('whatsapp_spammer.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

class WhatsAppSpammer:
    def __init__(self):
        self.contacts = []
        self.is_spamming = False
        self.spam_thread = None
        self.setup_directories()
    
    def setup_directories(self):
        """Create necessary directories"""
        os.makedirs('logs', exist_ok=True)
        os.makedirs('contacts', exist_ok=True)
    
    def add_contact(self, phone_number, name=""):
        """Add WhatsApp contact with validation"""
        phone_number = self.clean_phone_number(phone_number)
        
        if not self.validate_phone_number(phone_number):
            logging.error(f"Invalid phone number: {phone_number}")
            return False
        
        self.contacts.append({"phone": phone_number, "name": name})
        logging.info(f"Contact added: {name} ({phone_number})")
        return True
    
    def clean_phone_number(self, phone_number):
        """Clean and format phone number"""
        original_has_plus = phone_number.startswith('+')
        
        if original_has_plus:
            digits = ''.join(filter(str.isdigit, phone_number[1:]))
            cleaned = '+' + digits
        else:
            digits = ''.join(filter(str.isdigit, phone_number))
            
            if digits.startswith('233') and len(digits) > 3:
                cleaned = '+' + digits
            elif len(digits) == 9:
                cleaned = '+233' + digits
            else:
                cleaned = '+' + digits
        
        return cleaned
    
    def validate_phone_number(self, phone_number):
        """Validate phone number format"""
        if not phone_number.startswith('+'):
            return False
        
        digits = phone_number[1:]
        if not digits.isdigit():
            return False
        
        if phone_number.startswith('+233'):
            if len(digits) != 12:
                return False
        
        return True
    
    def send_whatsapp_message_ultra_fast(self, phone_number, message):
        """ULTRA-FAST direct method for spamming"""
        try:
            import urllib.parse
            encoded_message = urllib.parse.quote(message)
            url = f"https://web.whatsapp.com/send?phone={phone_number[1:]}&text={encoded_message}"
            
            # Open in browser (reuse same tab for speed)
            webbrowser.open(url)
            time.sleep(3)  # Minimal wait for page load
            
            # Send message
            pyautogui.press('enter')
            time.sleep(0.1)  # Very short wait
            
            # Don't close tab to keep it fast
            # pyautogui.hotkey('ctrl', 'w')
            
            return True
        except Exception as e:
            logging.error(f"Ultra-fast send failed: {e}")
            return False
    
    def send_whatsapp_message_instant(self, phone_number, message):
        """Fast instant method"""
        try:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=message,
                wait_time=3,  # Minimal wait
                tab_close=True,
                close_time=1
            )
            return True
        except Exception as e:
            logging.error(f"Instant send failed: {e}")
            return False
    
    def start_ultra_spam(self, phone_number, message, delay=0.005):
        """Start ultra-fast spamming in a separate thread"""
        self.is_spamming = True
        message_count = 0
        start_time = time.time()
        
        logging.info(f"🚀 STARTING ULTRA SPAM MODE")
        logging.info(f"📱 Target: {phone_number}")
        logging.info(f"💬 Message: {message}")
        logging.info(f"⚡ Delay: {delay} seconds")
        logging.info(f"🛑 To stop: Press Ctrl+C or type 'stop'")
        
        try:
            while self.is_spamming:
                try:
                    # Use ultra-fast direct method
                    if self.send_whatsapp_message_ultra_fast(phone_number, message):
                        message_count += 1
                        
                        # Show progress every 10 messages
                        if message_count % 10 == 0:
                            elapsed = time.time() - start_time
                            rate = message_count / elapsed if elapsed > 0 else 0
                            logging.info(f"📨 Sent {message_count} messages | Rate: {rate:.1f} msg/sec")
                    
                    # Ultra-short delay
                    time.sleep(delay)
                    
                except Exception as e:
                    logging.error(f"Spam error: {e}")
                    # Continue spamming despite errors
                    time.sleep(0.1)
                    
        except KeyboardInterrupt:
            self.is_spamming = False
            logging.info("🛑 Spamming stopped by user")
        
        elapsed = time.time() - start_time
        final_rate = message_count / elapsed if elapsed > 0 else 0
        
        logging.info(f"✅ SPAMMING COMPLETED")
        logging.info(f"📊 Total messages: {message_count}")
        logging.info(f"⏱️  Total time: {elapsed:.1f} seconds")
        logging.info(f"⚡ Average rate: {final_rate:.1f} messages/second")
        
        return message_count
    
    def start_spam_thread(self, phone_number, message, delay=0.005):
        """Start spamming in a separate thread"""
        if self.is_spamming:
            logging.warning("⚠️ Spamming is already running!")
            return
        
        self.spam_thread = threading.Thread(
            target=self.start_ultra_spam,
            args=(phone_number, message, delay)
        )
        self.spam_thread.daemon = True
        self.spam_thread.start()
        
        logging.info("🧵 Spam thread started")
    
    def stop_spam(self):
        """Stop the spamming"""
        if self.is_spamming:
            self.is_spamming = False
            logging.info("🛑 Stopping spam...")
            
            if self.spam_thread and self.spam_thread.is_alive():
                self.spam_thread.join(timeout=5)
                logging.info("✅ Spam thread stopped")
        else:
            logging.info("ℹ️ No active spam to stop")

def main():
    """Main function for ultra-fast WhatsApp spamming"""
    print("\n" + "="*70)
    print("💥 ULTRA-FAST WHATSAPP SPAMMER")
    print("="*70)
    print("⚡ Sends messages every 0.005 seconds")
    print("🚀 EXTREME SPAMMING MODE")
    print("="*70)
    print("⚠️  WARNING: Use responsibly! May get your number temporarily banned!")
    print("="*70)
    
    spammer = WhatsAppSpammer()
    
    # Get target number (your own number)
    print("\n🎯 ENTER YOUR PHONE NUMBER TO SPAM YOURSELF:")
    print("🇬🇭 GHANA NUMBER FORMATS:")
    print("  - +233532661209    (Full international)")
    print("  - 0532661209       (Local with 0)")
    print("  - 532661209        (Local without 0)")
    
    while True:
        phone = input("\n📱 Enter YOUR phone number: ").strip()
        if phone:
            if spammer.add_contact(phone, "SELF"):
                final_phone = spammer.contacts[0]['phone']
                print(f"✅ Target set: {final_phone}")
                break
            else:
                print("❌ Invalid number. Please try again.")
        else:
            print("❌ Please enter a phone number.")
    
    # Get message
    print("\n💬 ENTER SPAM MESSAGE:")
    default_message = "SPAM TEST 🚀"
    
    print(f"Default message: {default_message}")
    use_default = input("Use this message? (y/n): ").strip().lower()
    
    if use_default == 'y':
        message = default_message
    else:
        message = input("Enter your spam message: ").strip() or default_message
    
    # Get delay (ultra-fast mode)
    print("\n⚡ SPAM SPEED SETTINGS:")
    print("1. ULTRA FAST (0.005 seconds) - EXTREME")
    print("2. Very Fast (0.01 seconds) - INTENSE") 
    print("3. Fast (0.05 seconds) - HEAVY")
    print("4. Custom delay")
    
    speed_choice = input("Choose speed (1-4): ").strip()
    
    if speed_choice == "1":
        delay = 0.005
    elif speed_choice == "2":
        delay = 0.01
    elif speed_choice == "3":
        delay = 0.05
    elif speed_choice == "4":
        try:
            custom_delay = float(input("Enter custom delay in seconds (e.g., 0.001): ").strip())
            delay = max(0.001, custom_delay)  # Minimum 0.001 seconds
        except:
            delay = 0.005
            print("⚠️  Invalid input, using ultra-fast (0.005s)")
    else:
        delay = 0.005
        print("⚠️  Invalid choice, using ultra-fast (0.005s)")
    
    # Final confirmation
    print(f"\n🎯 FINAL CONFIRMATION:")
    print(f"   Target: {spammer.contacts[0]['phone']}")
    print(f"   Message: {message}")
    print(f"   Delay: {delay} seconds")
    print(f"   Estimated rate: {1/delay:.0f} messages/second")
    
    print("\n⚠️  CRITICAL WARNINGS:")
    print("   • WhatsApp may TEMPORARILY BAN your number")
    print("   • Keep WhatsApp Web OPEN and ACTIVE")
    print("   • Do not interact with browser during spamming")
    print("   • Use at your own risk!")
    
    confirm = input("\n🚀 START EXTREME SPAMMING? (y/n): ").strip().lower()
    if confirm != 'y':
        print("👋 Operation cancelled.")
        return
    
    # Start spamming
    target_phone = spammer.contacts[0]['phone']
    
    print(f"\n💥 STARTING EXTREME SPAMMING...")
    print(f"📱 Target: {target_phone}")
    print(f"⚡ Speed: {1/delay:.0f} messages/second")
    print(f"💬 Message: {message}")
    print("\n🛑 TO STOP:")
    print("   • Press Ctrl+C")
    print("   • Or close the program")
    print("   • Or wait for potential ban")
    print("\n" + "="*70)
    
    try:
        # Start spamming
        spammer.start_spam_thread(target_phone, message, delay)
        
        # Keep main thread alive and listen for stop command
        while spammer.is_spamming:
            try:
                user_input = input("Type 'stop' to end spamming: ").strip().lower()
                if user_input == 'stop':
                    spammer.stop_spam()
                    break
                time.sleep(0.1)
            except KeyboardInterrupt:
                spammer.stop_spam()
                break
            except:
                # Continue running if input fails
                time.sleep(0.1)
                
    except KeyboardInterrupt:
        spammer.stop_spam()
    except Exception as e:
        logging.error(f"Main loop error: {e}")
        spammer.stop_spam()
    
    print("\n👋 Spammer shutdown complete.")

if __name__ == "__main__":
    main()