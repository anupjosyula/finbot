## greet what possible
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* ask_whatspossible
    - utter_what_possible

## thanks
* thank
    - utter_noworries
    - utter_anything_else

## thanks what possible
* thank
    - utter_noworries
    - utter_anything_else
* ask_whatspossible
    - utter_what_possible

## bye
* bye
    - utter_bye

## anything else? - yes
    - utter_anything_else
* affirm
    - utter_what_help

## anything else? - no
    - utter_anything_else
* deny
    - utter_thumbsup

## positive reaction
* react_positive
    - utter_react_positive

## negative reaction
* react_negative
    - utter_react_negative

## source code
* source_code
    - utter_source_code
    - utter_anything_else

## greet chitchat
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* chitchat
    - respond_chitchat

## greet chitchat what possible
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* chitchat
    - respond_chitchat
* ask_whatspossible
    - utter_what_possible

## chitchat
* chitchat
    - respond_chitchat

## deny chitchat
* chitchat
    - respond_chitchat
* deny
    - utter_nohelp

## more chitchat
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat

## greet askusername more chitchat what possible
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* ask_whatspossible
    - utter_what_possible

## askusername more chitchat
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat

## more askusername chitchat what possible
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* ask_whatspossible
    - utter_what_possible

## greet askusername greet chitchat
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* greet
    - utter_greet
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat

## greet askusername greet chitchat what possible
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* greet
    - utter_greet
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* ask_whatspossible
    - utter_what_possible

# additionaldetails
* additionallinks
    - utter_anything_else

# notvalidinputs
* out_of_scope
    - utter_canthelp
    - utter_what_possible
    - utter_nohelp

## greet askusername
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
    - utter_deny_accept
    
## greet weatherdetails
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* weather
    - utter_city
* cities
    - action_weather_api
    - utter_deny_accept
    
## greet askusername fbprelated
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* fbp
    - utter_fbp
    - utter_deny_accept
    
## greet askusername attendancerelated
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* attendance
    - utter_attendance
    - utter_deny_accept
    
##greet askusername infrastructure 
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* travelrealated
    - utter_travelrelated
    - utter_deny_accept

## greet askusername operations
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* operations
    - utter_operations
    - utter_deny_accept
 
## greet askusername travelrelated
* greet
    - utter_greet
    - utter_capture_username
* getuserdetails
    - utter_capture_empid
* getemployeedetails
    - utter_thanks_for_the_details
* infrastructure
    - utter_infrastructure
    - utter_deny_accept  
    
   
## askholidaycalendar
* holidaycalendar
    - utter_holidaycalendar_city

##leave
* types_of_leave
    - action_type_of_leave
    
## reminder_greet
* greet
    - utter_greet
* ask_remind_call
    - action_set_reminder

##ask phonenumber
* ask_phonenumber
    - utter_phonenumber

##sing_a_song
* sing_a_song
    - utter_song

##continentslist
* list_of_continents
    - action_sample_graphql

##resourcelistusinggraphql
* list_of_resources
    - action_agile_bot_graphql_resources_list