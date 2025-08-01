import PyPDF2
import os
import sys

def decrypt_and_save_pdf(input_pdf_path, output_pdf_path, password):
    """
    Decrypt a password-protected PDF and save it as an unprotected PDF.
    
    Args:
        input_pdf_path (str): Path to the encrypted PDF file
        output_pdf_path (str): Path where the decrypted PDF will be saved
        password (str): Password for the encrypted PDF
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if not os.path.exists(input_pdf_path):
            print(f"Error: Input file not found at {input_pdf_path}")
            return False
            
        with open(input_pdf_path, 'rb') as input_file:
            reader = PyPDF2.PdfReader(input_file)
            
            if not reader.is_encrypted:
                print("PDF is not encrypted. No decryption needed.")
                return False
                
            if reader.decrypt(password):
                writer = PyPDF2.PdfWriter()
                
                for page in reader.pages:
                    writer.add_page(page)
                
                os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
                
                with open(output_pdf_path, 'wb') as output_file:
                    writer.write(output_file)
                    
                print(f"PDF successfully decrypted and saved to: {output_pdf_path}")
                return True
            else:
                print("Incorrect password. Please try again.")
                return False
                
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_pdf_path}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    """Main function to handle command line usage"""
    if len(sys.argv) != 4:
        print("Usage: python pdf_decryptor.py <input_pdf> <output_pdf> <password>")
        print("Example: python pdf_decryptor.py encrypted.pdf decrypted.pdf mypassword")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]
    
    success = decrypt_and_save_pdf(input_pdf, output_pdf, password)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()