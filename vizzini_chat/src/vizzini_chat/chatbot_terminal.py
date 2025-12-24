from vizzini_chat.crew import VizziniChat

def main():
    crew = VizziniChat().crew()
    print("ברוכים הבאים לבוט קפה ויזיני! (להפסקה כתוב 'יציאה')")
    print("נציג: שלום! אני כאן לעזור לך למצוא את הקפה המושלם. בוא נתחיל!")
    print("")

    preferences_collected = False
    customer_preferences = {}
    recommended_blends = None

    while True:
        user_msg = input("לקוח: ").strip()
        if user_msg in ['יציאה', 'exit', 'EXIT', 'Exit']:
            print("נציג: להתראות!")
            break

        # Step 1: Gather customer preferences if not done
        if not preferences_collected:
            try:
                response = crew.gather_customer_preferences(inputs={'customer_message': user_msg})
                print("נציג:", response)
                # TODO: Detect if preferences are complete using your own logic or by parsing the response
                if any(end in response for end in ["סיימנו לאסוף את ההעדפות שלך", "ההעדפות שלך נקלטו"]):
                    preferences_collected = True
                    # Optionally extract the preferences here for further task steps (if CrewAI exposes structure)
            except Exception as e:
                print("נציג: שגיאה בביצוע המשימה. \n", str(e))
        # Step 2: Recommend blends after preferences are gathered
        elif not recommended_blends:
            try:
                response = crew.search_and_recommend_blends()
                print("נציג:", response)
                recommended_blends = True
            except Exception as e:
                print("נציג: שגיאה בביצוע ההמלצה. \n", str(e))
        else:
            # Optionally handle finalization task here (link/order phase)
            print("נציג: האם תרצה לצאת או להמשיך לשיחה חדשה?")

if __name__ == "__main__":
    main()
