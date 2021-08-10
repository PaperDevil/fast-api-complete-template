from typing import Optional
import phonenumbers


def get_phone_national_number(phone_number: Optional[str]) -> Optional[str]:
    if not phone_number:
        return None
    result = None
    if (
            (phone_number.startswith('9') and len(phone_number) == 10)
            or (phone_number.startswith(('79', '89')) and len(phone_number) == 11)
            or (phone_number.startswith(('+79',)) and len(phone_number) == 12)
    ):
        phone = phonenumbers.parse(phone_number, "RU")
        if phone.country_code == 7 and len(str(phone.national_number)) == 10:
            result = phone.national_number
    return str(result).replace(' ', '').strip()
