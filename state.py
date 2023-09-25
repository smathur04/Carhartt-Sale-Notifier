import process
import time
import text


def does_state_change():
    while True:
        current_state = process.process_scraped_data()
        time.sleep(60)
        new_state = process.process_scraped_data()
        if current_state != new_state:
            new_items = {}
            for key, value in new_state.items():
                if key not in current_state:
                    new_items[key] = value
            text.send_text(new_items)
