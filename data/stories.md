## story_1
* greet
    - utter_greet
## interactive_story_1
* greet
    - utter_greet
## interactive_story_1
* lecturer_schedule{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_whatsapp_number{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_whatsapp_number
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
* procedure{"type": "pendaftaran praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
* practicum_value{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_value
    - reset_slots
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* greet
    - utter_greet
* student_schedule{"day": "Kamis"}
    - slot{"day": "Kamis"}
    - action_student_schedule

## interactive_story_1
* lecturer_schedule{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
* lecturer_schedule{"lecturer": "aris", "day": "besok"}
    - slot{"day": "besok"}
    - slot{"lecturer": "aris"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
* lecturer_whatsapp_number{"lecturer": "rini"}
    - slot{"lecturer": "rini"}
    - action_lecturer_whatsapp_number
* lecturer_schedule{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_schedule{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_schedule
    - reset_slots
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_1
* lecturer_schedule{"lecturer": "fajar", "day": "besok"}
    - slot{"day": "besok"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "pangat"}
    - slot{"lecturer": "pangat"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"day": "Kamis", "lecturer": "luvia"}
    - slot{"day": "Kamis"}
    - slot{"lecturer": "luvia"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_location{"lecturer": "elson"}
    - slot{"lecturer": "elson"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* lecturer_schedule{"day": "besok", "lecturer": "sugi"}
    - slot{"day": "besok"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"day": "Jumat", "lecturer": "agyl"}
    - slot{"day": "Jumat"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* lecturer_schedule{"day": "besok", "lecturer": "aris"}
    - slot{"day": "besok"}
    - slot{"lecturer": "aris"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"day": "Kamis", "lecturer": "andre"}
    - slot{"day": "Kamis"}
    - slot{"lecturer": "andre"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_1
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* thank
    - utter_thank
* lecturer_whatsapp_number
    - utter_ask_lecturer_name
* lecturer{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer
    - slot{"lecturer": null}
* practicum_schedule{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_schedule
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_1
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* practicum_schedule{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_schedule
    - reset_slots
* registration_schedule{"type": "praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "ery"}
    - slot{"lecturer": "ery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_value{"practicum": "Sistem Jaringan Komputer"}
    - slot{"practicum": "Sistem Jaringan Komputer"}
    - action_practicum_value
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots

## interactive_story_2
* greet
    - utter_greet
* lecturer_location{"lecturer": "pangat"}
    - slot{"lecturer": "pangat"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* lecturer_location{"lecturer": "ery"}
    - slot{"lecturer": "ery"}
    - action_lecturer_location
* lecturer_whatsapp_number{"lecturer": "yusrida"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer_whatsapp_number
* lecturer_schedule{"lecturer": "ardi", "day": "besok"}
    - slot{"day": "besok"}
    - slot{"lecturer": "ardi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* practicum_schedule{"practicum": "Sistem Operasi"}
    - slot{"practicum": "Sistem Operasi"}
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* greet
    - utter_greet
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_2
* lecturer_whatsapp_number{"lecturer": "agung"}
    - slot{"lecturer": "agung"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_location{"lecturer": "aher"}
    - slot{"lecturer": "aher"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_schedule{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "pemrograman dasar"}
    - slot{"practicum": "pemrograman dasar"}
    - action_practicum_value
    - reset_slots
* registration_schedule{"type": "praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* greet
    - utter_greet
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_3
* lecturer_schedule{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_location{"lecturer": "yusrida"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number{"lecturer": "agus dar"}
    - slot{"lecturer": "agus dar"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "Sistem Jaringan Komputer"}
    - slot{"practicum": "Sistem Jaringan Komputer"}
    - action_practicum_value
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* greet
    - utter_greet
* thank
    - utter_thank
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_4
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* lecturer_location{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* practicum_schedule{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_value
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "kerja pratek"}
    - slot{"type": "kerja pratek"}
    - action_registration_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* greet
    - utter_greet
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_1
* practicum_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_practicum_schedule
    - reset_slots
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots
* registration_schedule{"type": "praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* lecturer_schedule{"lecturer": "gerry"}
    - slot{"lecturer": "gerry"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_2
* greet
    - utter_greet
* greet
    - utter_greet
* lecturer_schedule{"lecturer": "agung kridoyono", "day": "Rabu"}
    - slot{"day": "Rabu"}
    - slot{"lecturer": "agung kridoyono"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* procedure{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* practicum_value{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_value
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_3
* practicum_value
    - action_practicum_value
    - reset_slots
* practicum_value{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - action_practicum_value
    - reset_slots
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "habib", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "habib"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_schedule{"type": "praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "praktikum"}
    - action_practicum_schedule
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_4
* registration_schedule{"type": "praktikum", "practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* greet
    - utter_greet

## interactive_story_1
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_procedure
    - reset_slots
* lecturer_schedule{"lecturer": "agung kridoyono"}
    - slot{"lecturer": "agung kridoyono"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "gerry"}
    - slot{"lecturer": "gerry"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_2
* lecturer_schedule{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "muaaffaq"}
    - slot{"lecturer": "muaaffaq"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "sidqon"}
    - slot{"lecturer": "sidqon"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "agung", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "agung"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_3
* lecturer_location{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* practicum_schedule{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_schedule
    - reset_slots
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_4
* greet
    - utter_greet
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots

## interactive_story_5
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* student_schedule
    - action_student_schedule
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "ardi"}
    - slot{"lecturer": "ardi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "yusrida"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "yusrida", "day": "Senin"}
    - slot{"day": "Senin"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_1
* lecturer_schedule{"lecturer": "anton", "day": "Rabu"}
    - slot{"day": "Rabu"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "aher", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "aher"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "rini", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "rini"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_value{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_value
    - reset_slots
* practicum_value{"practicum": "Sistem Operasi"}
    - slot{"practicum": "Sistem Operasi"}
    - action_practicum_value
    - reset_slots
* lecturer_schedule{"lecturer": "agus dar"}
    - slot{"lecturer": "agus dar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"day": "besok", "lecturer": "agung"}
    - slot{"day": "besok"}
    - slot{"lecturer": "agung"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_schedule{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_schedule
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_3
* greet
    - utter_greet
* lecturer_schedule{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Dasar"}
    - slot{"practicum": "Pemrograman Dasar"}
    - action_practicum_value
    - reset_slots
* lecturer_schedule{"lecturer": "fajar", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* thank
    - utter_thank

## interactive_story_1
* lecturer_schedule{"lecturer": "agus hermanto"}
    - slot{"lecturer": "agus hermanto"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots

## interactive_story_1
* greet
    - utter_greet
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_schedule{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "yusrida", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "sugi", "day": "besok"}
    - slot{"day": "besok"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_value{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_value
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots
* practicum_schedule{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_schedule
    - reset_slots
* lecturer_location{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* thank
    - utter_thank

## interactive_story_1
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* lecturer_whatsapp_number
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_location
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots

## interactive_story_2
* lecturer_location
    - action_lecturer_location
    - slot{"ask_lecturer_location": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "fajar astuti"}
    - slot{"lecturer": "fajar astuti"}
    - action_lecturer
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_3
* lecturer_schedule{"day": "Kamis", "lecturer": "agus darwanto"}
    - slot{"day": "Kamis"}
    - slot{"lecturer": "agus darwanto"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* practicum_value{"practicum": "sistem operasi"}
    - slot{"practicum": "sistem operasi"}
    - action_practicum_value
    - reset_slots
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_1
* lecturer_whatsapp_number
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "fajar astuti"}
    - slot{"lecturer": "fajar astuti"}
    - action_lecturer
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_schedule{"lecturer": "fajar", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_value{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - action_practicum_value
    - reset_slots
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_2
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_procedure
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "yus"}
    - slot{"lecturer": "yus"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* lecturer_location
    - action_lecturer_location
    - slot{"ask_lecturer_location": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer
    - slot{"ask_lecturer_location": null}
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* thank
    - utter_thank

## interactive_story_1
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* practicum_value
    - action_practicum_value
    - reset_slots
* practicum_value
    - action_practicum_value
    - reset_slots

## interactive_story_1
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_2
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* greet
    - utter_greet

## interactive_story_3
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* lecturer{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_4
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* lecturer_location{"lecturer": "agung"}
    - slot{"lecturer": "agung"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_5
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "aris", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "aris"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_6
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_7
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots

## interactive_story_8
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots

## interactive_story_1
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
* practicum_schedule
    - action_practicum_schedule
    - reset_slots

## interactive_story_2
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* practicum_value{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - action_practicum_value
    - reset_slots

## interactive_story_3
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_4
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots

## interactive_story_5
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots

## interactive_story_6
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_7
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots

## interactive_story_1
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule

## interactive_story_2
* goodbye
    - utter_goodbye
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots

## interactive_story_3
* goodbye
    - utter_goodbye
* goodbye
    - utter_goodbye

## interactive_story_4
* goodbye
    - utter_goodbye
* greet
    - utter_greet

## interactive_story_5
* goodbye
    - utter_goodbye
* lecturer{"lecturer": "agung"}
    - slot{"lecturer": "agung"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_6
* goodbye
    - utter_goodbye
* lecturer_location{"lecturer": "ardi"}
    - slot{"lecturer": "ardi"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_7
* goodbye
    - utter_goodbye
* lecturer_schedule{"lecturer": "fir", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "fir"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_8
* goodbye
    - utter_goodbye
* lecturer_whatsapp_number{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_9
* goodbye
    - utter_goodbye
* practicum_schedule
    - action_practicum_schedule
    - reset_slots

## interactive_story_10
* goodbye
    - utter_goodbye
* practicum_value{"practicum": "pemrograman dasar"}
    - slot{"practicum": "pemrograman dasar"}
    - action_practicum_value
    - reset_slots

## interactive_story_11
* goodbye
    - utter_goodbye
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_12
* goodbye
    - utter_goodbye
* registration_schedule{"type": "praktikum", "practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots

## interactive_story_13
* goodbye
    - utter_goodbye
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots

## interactive_story_14
* goodbye
    - utter_goodbye
* thank
    - utter_thank

## interactive_story_15
* goodbye
    - utter_goodbye
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule

## interactive_story_1
* greet
    - utter_greet
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* greet
    - utter_greet

## interactive_story_4
* greet
    - utter_greet
* lecturer{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_5
* greet
    - utter_greet
* lecturer_location{"lecturer": "aidil"}
    - slot{"lecturer": "aidil"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_6
* greet
    - utter_greet
* lecturer_schedule{"lecturer": "anton", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_7
* greet
    - utter_greet
* lecturer_whatsapp_number{"lecturer": "agung"}
    - slot{"lecturer": "agung"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_8
* greet
    - utter_greet
* practicum_schedule
    - action_practicum_schedule
    - reset_slots

## interactive_story_9
* greet
    - utter_greet
* practicum_value{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_value
    - reset_slots

## interactive_story_10
* greet
    - utter_greet
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_11
* greet
    - utter_greet
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots

## interactive_story_12
* greet
    - utter_greet
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots

## interactive_story_13
* greet
    - utter_greet
* thank
    - utter_thank

## interactive_story_14
* greet
    - utter_greet
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule

## interactive_story_1
* lecturer{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer
    - slot{"lecturer": null}
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* lecturer{"lecturer": "yusrida"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer
    - slot{"lecturer": null}
* goodbye
    - utter_goodbye

## interactive_story_3
* lecturer{"lecturer": "aris sudaryanto"}
    - slot{"lecturer": "aris sudaryanto"}
    - action_lecturer
    - slot{"lecturer": null}
* greet
    - utter_greet

## interactive_story_4
* lecturer{"lecturer": "fajar astuti"}
    - slot{"lecturer": "fajar astuti"}
    - action_lecturer
    - slot{"lecturer": null}
* lecturer{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_5
* lecturer{"lecturer": "aidil"}
    - slot{"lecturer": "aidil"}
    - action_lecturer
    - slot{"lecturer": null}
* lecturer_location{"lecturer": "aidil"}
    - slot{"lecturer": "aidil"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_6
* lecturer{"lecturer": "agyl ardi"}
    - slot{"lecturer": "agyl ardi"}
    - action_lecturer
    - slot{"lecturer": null}
* lecturer_schedule{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_7
* lecturer{"lecturer": "firdaus"}
    - slot{"lecturer": "firdaus"}
    - action_lecturer
    - slot{"lecturer": null}
* lecturer_whatsapp_number{"lecturer": "firdaus"}
    - slot{"lecturer": "firdaus"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_8
* lecturer{"lecturer": "anang pramono"}
    - slot{"lecturer": "anang pramono"}
    - action_lecturer
    - slot{"lecturer": null}
* lecturer_schedule{"lecturer": "anang"}
    - slot{"lecturer": "anang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_9
* lecturer{"lecturer": "agus hermanto"}
    - slot{"lecturer": "agus hermanto"}
    - action_lecturer
    - slot{"lecturer": null}
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_10
* lecturer{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer
    - slot{"lecturer": null}
* practicum_value{"practicum": "Sistem Jaringan Komputer"}
    - slot{"practicum": "Sistem Jaringan Komputer"}
    - action_practicum_value
    - reset_slots

## interactive_story_11
* lecturer{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer
    - slot{"lecturer": null}
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_12
* lecturer{"lecturer": "rini"}
    - slot{"lecturer": "rini"}
    - action_lecturer
    - slot{"lecturer": null}
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots

## interactive_story_13
* lecturer{"lecturer": "sherli"}
    - slot{"lecturer": "sherli"}
    - action_lecturer
    - slot{"lecturer": null}
* student_schedule{"day": "lusa"}
    - slot{"day": "lusa"}
    - action_student_schedule
    - reset_slots

## interactive_story_14
* lecturer{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer
    - slot{"lecturer": null}
* thank
    - utter_thank

## interactive_story_15
* lecturer{"lecturer": "ardi"}
    - slot{"lecturer": "ardi"}
    - action_lecturer
    - slot{"lecturer": null}
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* lecturer_location{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* lecturer_location{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* goodbye
    - utter_goodbye

## interactive_story_3
* lecturer_location{"lecturer": "yusrida"}
    - slot{"lecturer": "yusrida"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* greet
    - utter_greet

## interactive_story_4
* lecturer_location{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_5
* lecturer_location{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_6
* lecturer_location{"lecturer": "sidqon"}
    - slot{"lecturer": "sidqon"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_schedule{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_7
* lecturer_location{"lecturer": "ery"}
    - slot{"lecturer": "ery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_whatsapp_number
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_8
* lecturer_location{"lecturer": "agus dar"}
    - slot{"lecturer": "agus dar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* practicum_schedule
    - action_practicum_schedule
    - reset_slots

## interactive_story_9
* lecturer_location{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* practicum_value
    - action_practicum_value
    - reset_slots

## interactive_story_10
* lecturer_location{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots

## interactive_story_11
* lecturer_location{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots

## interactive_story_12
* lecturer_location{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots

## interactive_story_13
* lecturer_location{"lecturer": "aris"}
    - slot{"lecturer": "aris"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* thank
    - utter_thank

## interactive_story_14
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* lecturer_schedule{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule

## interactive_story_2
* lecturer_schedule{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_3
* lecturer_schedule{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_4
* lecturer_schedule{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* greet
    - utter_greet

## interactive_story_5
* lecturer_schedule{"lecturer": "anton", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_6
* lecturer_schedule{"lecturer": "ery"}
    - slot{"lecturer": "ery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_location{"lecturer": "ery"}
    - slot{"lecturer": "ery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_7
* lecturer_schedule{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_schedule{"day": "Kamis", "lecturer": "agus dar"}
    - slot{"day": "Kamis"}
    - slot{"lecturer": "agus dar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_8
* lecturer_schedule{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_9
* lecturer_schedule{"lecturer": "aidil", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "aidil"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_10
* lecturer_schedule{"lecturer": "anang", "day": "besok"}
    - slot{"day": "besok"}
    - slot{"lecturer": "anang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* practicum_value{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_value
    - reset_slots

## interactive_story_11
* lecturer_schedule{"lecturer": "supangat"}
    - slot{"lecturer": "supangat"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots

## interactive_story_12
* lecturer_schedule{"lecturer": "agus hermanto", "day": "Selasa"}
    - slot{"day": "Selasa"}
    - slot{"lecturer": "agus hermanto"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots

## interactive_story_13
* lecturer_schedule{"day": "Senin", "lecturer": "fir"}
    - slot{"day": "Senin"}
    - slot{"lecturer": "fir"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots

## interactive_story_14
* lecturer_schedule{"day": "Rabu", "lecturer": "gery"}
    - slot{"day": "Rabu"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* thank
    - utter_thank

## interactive_story_15
* lecturer_schedule{"lecturer": "habib", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "habib"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* lecturer_schedule{"lecturer": "fajar", "day": "hari ini"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* thank
    - utter_thank
* lecturer_schedule{"day": "hari ini", "lecturer": "gery"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_2
* lecturer_schedule{"lecturer": "putri"}
    - slot{"lecturer": "putri"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots

## interactive_story_3
* lecturer_whatsapp_number{"lecturer": "supangat"}
    - slot{"lecturer": "supangat"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_4
* lecturer_whatsapp_number{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* goodbye
    - utter_goodbye

## interactive_story_5
* lecturer_whatsapp_number{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* greet
    - utter_greet

## interactive_story_6
* lecturer_whatsapp_number{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer{"lecturer": "agus dar"}
    - slot{"lecturer": "agus dar"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_7
* lecturer_whatsapp_number{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_location
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_8
* lecturer_whatsapp_number{"lecturer": "pangat"}
    - slot{"lecturer": "pangat"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_schedule{"day": "hari ini", "lecturer": "sidqon"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "sidqon"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_9
* lecturer_whatsapp_number{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_whatsapp_number{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_10
* lecturer_whatsapp_number{"lecturer": "agung"}
    - slot{"lecturer": "agung"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* practicum_schedule{"practicum": "Dasar Komputer dan Internet"}
    - slot{"practicum": "Dasar Komputer dan Internet"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_11
* lecturer_whatsapp_number{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* practicum_value{"practicum": "Dasar Komputer dan Internet"}
    - slot{"practicum": "Dasar Komputer dan Internet"}
    - action_practicum_value
    - reset_slots

## interactive_story_12
* lecturer_whatsapp_number{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_13
* lecturer_whatsapp_number{"lecturer": "aris"}
    - slot{"lecturer": "aris"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots

## interactive_story_14
* lecturer_whatsapp_number{"lecturer": "aidil"}
    - slot{"lecturer": "aidil"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots

## interactive_story_15
* lecturer_whatsapp_number{"lecturer": "fridi"}
    - slot{"lecturer": "fridi"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* thank
    - utter_thank

## interactive_story_16
* lecturer_whatsapp_number{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_17
* practicum_schedule{"practicum": "Sistem Operasi"}
    - slot{"practicum": "Sistem Operasi"}
    - action_practicum_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots

## interactive_story_18
* practicum_schedule{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_schedule
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_19
* procedure{"practicum": "Sistem Jaringan Komputer"}
    - slot{"practicum": "Sistem Jaringan Komputer"}
    - action_practicum_schedule
    - reset_slots
* greet
    - utter_greet

## interactive_story_20
* practicum_schedule{"practicum": "Dasar Komputer dan Internet"}
    - slot{"practicum": "Dasar Komputer dan Internet"}
    - action_practicum_schedule
    - reset_slots
* lecturer{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_21
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* lecturer_location{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_22
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_23
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "agus hermanto"}
    - slot{"lecturer": "agus hermanto"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_24
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots
* practicum_schedule{"practicum": "Manajemen Data dan Informasi"}
    - slot{"practicum": "Manajemen Data dan Informasi"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_25
* practicum_schedule{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - action_practicum_value
    - reset_slots

## interactive_story_26
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_27
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots
* registration_schedule{"practicum": "Dasar Komputer dan Internet"}
    - slot{"practicum": "Dasar Komputer dan Internet"}
    - action_registration_schedule
    - reset_slots

## interactive_story_28
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots

## interactive_story_29
* practicum_schedule{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_30
* practicum_schedule{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_schedule
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_31
* practicum_value{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_value
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_32
* practicum_value{"practicum": "Manajemen Data dan Informasi"}
    - slot{"practicum": "Manajemen Data dan Informasi"}
    - action_practicum_value
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_33
* practicum_value{"practicum": "Sistem Operasi"}
    - slot{"practicum": "Sistem Operasi"}
    - action_practicum_value
    - reset_slots
* greet
    - utter_greet

## interactive_story_34
* practicum_value
    - action_practicum_value
    - reset_slots
* lecturer{"lecturer": "rini"}
    - slot{"lecturer": "rini"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_35
* practicum_value
    - action_practicum_value
    - reset_slots
* lecturer_location{"lecturer": "harini"}
    - slot{"lecturer": "harini"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_36
* practicum_value{"practicum": "Pengolahan Citra Digital"}
    - slot{"practicum": "Pengolahan Citra Digital"}
    - action_practicum_value
    - reset_slots
* lecturer_schedule{"lecturer": "andre", "day": "besok"}
    - slot{"day": "besok"}
    - slot{"lecturer": "andre"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_37
* practicum_value{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_value
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "ery"}
    - slot{"lecturer": "ery"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_38
* practicum_value{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_value
    - reset_slots
* practicum_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_39
* practicum_value{"practicum": "Pemrograman Dasar"}
    - slot{"practicum": "Pemrograman Dasar"}
    - action_practicum_value
    - reset_slots
* practicum_value{"practicum": "Pemrogaman Dasar"}
    - slot{"practicum": "Pemrogaman Dasar"}
    - action_practicum_value
    - reset_slots

## interactive_story_40
* practicum_value{"practicum": "Mikroprosessor"}
    - slot{"practicum": "Mikroprosessor"}
    - action_practicum_value
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots

## interactive_story_41
* practicum_value{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - action_practicum_value
    - reset_slots
* registration_schedule{"type": "praktikum", "practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots

## interactive_story_42
* practicum_value{"practicum": "Rangkaian Logika"}
    - slot{"practicum": "Rangkaian Logika"}
    - action_practicum_value
    - reset_slots
* student_schedule{"day": "Kamis"}
    - slot{"day": "Kamis"}
    - action_student_schedule
    - reset_slots

## interactive_story_43
* practicum_value{"practicum": "Sistem Jaringan Komputer"}
    - slot{"practicum": "Sistem Jaringan Komputer"}
    - action_practicum_value
    - reset_slots
* thank
    - utter_thank

## interactive_story_44
* practicum_value{"practicum": "Rangkaian Logika"}
    - slot{"practicum": "Rangkaian Logika"}
    - action_practicum_value
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_3
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* greet
    - utter_greet

## interactive_story_4
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* lecturer{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_5
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* lecturer_location{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_6
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* lecturer_schedule{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_7
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_8
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* practicum_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_9
* practicum_value{"practicum": "pemrograman lanjut"}
    - slot{"practicum": "pemrograman lanjut"}

## interactive_story_10
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* practicum_value{"practicum": "pemrograman lanjut"}
    - slot{"practicum": "pemrograman lanjut"}
    - action_practicum_value
    - reset_slots

## interactive_story_11
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots

## interactive_story_12
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots

## interactive_story_13
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots
* student_schedule{"day": "Kamis"}
    - slot{"day": "Kamis"}
    - action_student_schedule
    - reset_slots

## interactive_story_14
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots
* thank
    - utter_thank

## interactive_story_15
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots

## interactive_story_16
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_17
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_18
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots
* greet
    - utter_greet

## interactive_story_19
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* lecturer{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_20
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots
* lecturer_location{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_21
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "supangat", "day": "Rabu"}
    - slot{"day": "Rabu"}
    - slot{"lecturer": "supangat"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_22
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "ardi"}
    - slot{"lecturer": "ardi"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_23
* registration_schedule{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_registration_schedule
    - reset_slots
* practicum_schedule
    - action_practicum_schedule
    - reset_slots

## interactive_story_24
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots

## interactive_story_25
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_26
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots

## interactive_story_27
* registration_schedule{"type": "praktikum", "practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots
* student_schedule{"day": "Selasa"}
    - slot{"day": "Selasa"}
    - action_student_schedule
    - reset_slots

## interactive_story_28
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_29
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_1
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}

## interactive_story_2
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* greet
    - utter_greet

## interactive_story_3
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* lecturer{"lecturer": "andre"}
    - slot{"lecturer": "andre"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_4
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* lecturer_location{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_5
* student_schedule{"day": "besok", "time": "jam"}
    - slot{"day": "besok"}
    - slot{"time": "jam"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "fajar", "time": "jam"}
    - slot{"lecturer": "fajar"}
    - slot{"time": "jam"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
    - reset_slots

## interactive_story_6
* student_schedule{"day": "besok", "time": "jam"}
    - slot{"day": "besok"}
    - slot{"time": "jam"}
    - slot{"day": "besok"}
    - slot{"time": "jam"}
    - action_student_schedule
    - reset_slots

## interactive_story_1
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule

## interactive_story_2
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"time": "selanjutnya", "lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_3
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"time": "selanjutnya", "lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_4
* lecturer_schedule
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "ardi"}
    - slot{"lecturer": "ardi"}
    - action_lecturer
    - slot{"ask_lecturer_location": null}

## interactive_story_5
* student_schedule{"day": "besok", "time": "jam"}
    - slot{"day": "besok"}
    - slot{"time": "jam"}
    - action_student_schedule
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "agyl"}
    - slot{"lecturer": "agyl"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_6
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* practicum_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_7
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* practicum_value{"practicum": "Sistem Operasi"}
    - slot{"practicum": "Sistem Operasi"}
    - action_practicum_value
    - reset_slots

## interactive_story_8
* student_schedule{"day": "kemarin"}
    - slot{"day": "kemarin"}
    - action_student_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots

## interactive_story_9
* student_schedule{"day": "Kamis"}
    - slot{"day": "Kamis"}
    - action_student_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots

## interactive_story_10
* student_schedule{"day": "Jumat"}
    - slot{"day": "Jumat"}
    - action_student_schedule
    - reset_slots
* student_schedule{"day": "Senin"}
    - slot{"day": "Senin"}
    - action_student_schedule
    - reset_slots

## interactive_story_11
* student_schedule{"day": "Rabu"}
    - slot{"day": "Rabu"}
    - action_student_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_12
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* thank
    - utter_thank
* exam_schedule{"exam": "uts"}
    - slot{"exam": "uts"}
    - action_exam_schedule
    - reset_slots

## interactive_story_2
* thank
    - utter_thank
* goodbye
    - utter_goodbye

## interactive_story_3
* thank
    - utter_thank
* greet
    - utter_greet

## interactive_story_4
* thank
    - utter_thank
* lecturer{"lecturer": "luvia"}
    - slot{"lecturer": "luvia"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_5
* thank
    - utter_thank
* lecturer_location{"lecturer": "agung"}
    - slot{"lecturer": "agung"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_6
* thank
    - utter_thank
* lecturer_schedule{"lecturer": "sugi", "time": "selanjutnya"}
    - slot{"lecturer": "sugi"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_7
* thank
    - utter_thank
* lecturer_whatsapp_number{"lecturer": "supangat"}
    - slot{"lecturer": "supangat"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_8
* thank
    - utter_thank
* practicum_schedule{"practicum": "Rangkaian Logika"}
    - slot{"practicum": "Rangkaian Logika"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_9
* thank
    - utter_thank
* practicum_value{"practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_value
    - reset_slots

## interactive_story_10
* thank
    - utter_thank
* procedure{"type": "pendaftaran praktikum"}
    - slot{"type": "pendaftaran praktikum"}
    - action_procedure
    - reset_slots

## interactive_story_11
* thank
    - utter_thank
* registration_schedule{"type": "praktikum", "practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - slot{"type": "praktikum"}
    - action_registration_schedule
    - reset_slots

## interactive_story_12
* thank
    - utter_thank
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots

## interactive_story_13
* thank
    - utter_thank
* thank
    - utter_thank

## interactive_story_14
* thank
    - utter_thank
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_15
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* exam_schedule{"exam": "uas"}
    - slot{"exam": "uas"}
    - action_exam_schedule
    - reset_slots

## interactive_story_16
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* goodbye
    - utter_goodbye

## interactive_story_17
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* greet
    - utter_greet

## interactive_story_18
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* lecturer{"lecturer": "ardi"}
    - slot{"lecturer": "ardi"}
    - action_lecturer
    - slot{"lecturer": null}

## interactive_story_19
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_20
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* lecturer_schedule{"day": "kemarin", "lecturer": "anton"}
    - slot{"day": "kemarin"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_21
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* lecturer_whatsapp_number{"lecturer": "anang"}
    - slot{"lecturer": "anang"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_22
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* practicum_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_practicum_schedule
    - reset_slots

## interactive_story_23
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Lanjut"}
    - slot{"practicum": "Pemrograman Lanjut"}
    - action_practicum_value
    - reset_slots

## interactive_story_24
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* procedure{"type": "pendaftaran kerja praktek"}
    - slot{"type": "pendaftaran kerja praktek"}
    - action_procedure
    - reset_slots

## interactive_story_25
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots

## interactive_story_26
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots

## interactive_story_27
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* thank
    - utter_thank

## interactive_story_28
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"time": "selanjutnya", "lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "nuril", "time": "sebelumnya"}
    - slot{"lecturer": "nuril"}
    - slot{"time": "sebelumnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_1
* lecturer_schedule
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "aidil"}
    - slot{"lecturer": "aidil"}
    - action_lecturer
    - slot{"ask_lecturer_schedule": null}
* lecturer_whatsapp_number
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}

## interactive_story_2
* lecturer_schedule
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": true}
    - utter_ask_lecturer_name
* lecturer_schedule{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_3
* lecturer_schedule
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"time": "selanjutnya", "lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "fajar", "time": "selanjutnya"}
    - slot{"lecturer": "fajar"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_1
* lecturer_schedule{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer_schedule

## interactive_story_2
* lecturer_schedule{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"day": "hari ini", "lecturer": "fajar"}
    - slot{"day": "hari ini"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* practicum_value{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - slot{"practicum": "Komputer Grafik dan Visualisasi Data"}
    - action_practicum_value
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
* lecturer_schedule
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": true}
    - utter_ask_lecturer_name
* lecturer{"lecturer": "agyl rahmadi"}
    - slot{"lecturer": "agyl rahmadi"}
    - action_lecturer
    - slot{"ask_lecturer_schedule": null}

## interactive_story_1
* lecturer_schedule{"time": "selanjutnya", "lecturer": "aris"}
    - slot{"lecturer": "aris"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"day": "Senin"}
    - slot{"day": "Senin"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "habib"}
    - slot{"lecturer": "habib"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_2
* lecturer_schedule{"lecturer": "aher"}
    - slot{"lecturer": "aher"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "yus"}
    - slot{"lecturer": "yus"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_1
* student_schedule{"day": "hari ini"}
    - slot{"day": "hari ini"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"time": "selanjutnya", "lecturer": "aris"}
    - slot{"lecturer": "aris"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"day": "Senin"}
    - slot{"day": "Senin"}
    - action_student_schedule
    - reset_slots
* student_schedule{"day": "besok"}
    - slot{"day": "besok"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "anang"}
    - slot{"lecturer": "anang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "aris"}
    - slot{"lecturer": "aris"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_1
* lecturer_schedule{"time": "selanjutnya", "lecturer": "aris"}
    - slot{"lecturer": "aris"}
    - slot{"time": "selanjutnya"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* lecturer_location{"lecturer": "sugi"}
    - slot{"lecturer": "sugi"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "aher"}
    - slot{"lecturer": "aher"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_1
* lecturer_schedule{"lecturer": "erry"}
    - slot{"lecturer": "erry"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_whatsapp_number{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_whatsapp_number{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_whatsapp_number{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* lecturer_whatsapp_number{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* practicum_schedule{"practicum": "Pengembangan Teknologi Mobile"}
    - slot{"practicum": "Pengembangan Teknologi Mobile"}
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "Pemrograman Dasar"}
    - slot{"practicum": "Pemrograman Dasar"}
    - action_practicum_value
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_registration_schedule
    - reset_slots
* student_schedule{"time": "selanjutnya"}
    - slot{"time": "selanjutnya"}
    - action_student_schedule
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "tkp"}
    - slot{"type": "tkp"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots

## interactive_story_1
* student_schedule{"time": "sekarang"}
    - slot{"time": "sekarang"}
    - action_student_schedule
    - reset_slots
* student_schedule{"time": "sekarang"}
    - slot{"time": "sekarang"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "aidil", "time": "sekarang"}
    - slot{"lecturer": "aidil"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "agyl", "time": "sekarang"}
    - slot{"lecturer": "agyl"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"time": "sekarang", "lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"time": "saat ini"}
    - slot{"time": "saat ini"}
    - action_student_schedule
    - reset_slots

## interactive_story_2
* lecturer_schedule{"lecturer": "fajar", "time": "sekarang"}
    - slot{"lecturer": "fajar"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_location{"lecturer": "nuril", "time": "sekarang"}
    - slot{"lecturer": "nuril"}
    - slot{"time": "sekarang"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_1
* lecturer_schedule{"lecturer": "habib", "time": "sekarang"}
    - slot{"lecturer": "habib"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"time": "sekarang"}
    - slot{"time": "sekarang"}
    - action_student_schedule
    - reset_slots
* student_schedule{"time": "sekarang"}
    - slot{"time": "sekarang"}
    - action_student_schedule
    - reset_slots

## interactive_story_1
* lecturer_location{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_2
* lecturer_location{"lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "agyl rahmadi"}
    - slot{"lecturer": "agyl rahmadi"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "nuril esti"}
    - slot{"lecturer": "nuril esti"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "astuti"}
    - slot{"lecturer": "astuti"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_1
* lecturer_location{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "fajar astuti"}
    - slot{"lecturer": "fajar astuti"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "anton", "time": "sekarang"}
    - slot{"lecturer": "anton"}
    - slot{"time": "sekarang"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_schedule{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}

## interactive_story_2
* lecturer_location{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - slot{"lecturer": "anton"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "fajar astuti"}
    - slot{"lecturer": "fajar astuti"}
    - slot{"lecturer": "fajar astuti"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "anton", "time": "sekarang"}
    - slot{"lecturer": "anton"}
    - slot{"time": "sekarang"}
    - slot{"lecturer": "anton"}
    - slot{"time": "sekarang"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "nuril"}
    - slot{"lecturer": "nuril"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "yus"}
    - slot{"lecturer": "yus"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_location{"lecturer": "muaaffaq"}
    - slot{"lecturer": "muaaffaq"}
    - action_lecturer_location
    - slot{"ask_lecturer_location": null}
* lecturer_schedule{"lecturer": "gery"}
    - slot{"lecturer": "gery"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "rini"}
    - slot{"lecturer": "rini"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "fajar"}
    - slot{"lecturer": "fajar"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_1
* lecturer_schedule{"time": "sekarang", "lecturer": "sugiono"}
    - slot{"lecturer": "sugiono"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "sugiono", "time": "sekarang"}
    - slot{"lecturer": "sugiono"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "sugiono", "time": "sekarang"}
    - slot{"lecturer": "sugiono"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "anton", "time": "sekarang"}
    - slot{"lecturer": "anton"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* student_schedule{"time": "sekarang"}
    - slot{"time": "sekarang"}
    - action_student_schedule
    - reset_slots
* student_schedule{"time": "sekarang"}
    - slot{"time": "sekarang"}
    - action_student_schedule
    - reset_slots
* lecturer_schedule{"lecturer": "nuril", "time": "sekarang"}
    - slot{"lecturer": "nuril"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "nuril", "time": "sekarang"}
    - slot{"lecturer": "nuril"}
    - slot{"time": "sekarang"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}

## interactive_story_2
* trial_schedule{"type": "tugas akhir"}
    - slot{"type": "tugas akhir"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "tugas akhir"}
    - slot{"type": "tugas akhir"}
    - action_trial_schedule
    - reset_slots
* trial_schedule{"type": "tugas akhirnya"}
    - slot{"type": "tugas akhirnya"}
    - action_trial_schedule
    - reset_slots
* procedure{"type": "pendaftaran tugas akhir"}
    - slot{"type": "pendaftaran tugas akhir"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran tugas akhir"}
    - slot{"type": "pendaftaran tugas akhir"}
    - action_procedure
    - reset_slots
* procedure{"type": "pendaftaran tugas akhir"}
    - slot{"type": "pendaftaran tugas akhir"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "tugas akhir"}
    - slot{"type": "tugas akhir"}
    - action_registration_schedule
    - reset_slots

## interactive_story_1
* lecturer_schedule{"lecturer": "erry"}
    - slot{"lecturer": "erry"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_schedule{"lecturer": "eri"}
    - slot{"lecturer": "eri"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* practicum_schedule
    - action_practicum_schedule
    - reset_slots
* procedure{"type": "pendaftaran tkp"}
    - slot{"type": "pendaftaran tkp"}
    - action_procedure
    - reset_slots
* registration_schedule{"type": "pendaftaran praktikum", "practicum": "Pengembangan Teknologi Website"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - slot{"type": "pendaftaran praktikum"}
    - action_registration_schedule
    - reset_slots
* registration_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_registration_schedule
    - reset_slots
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* student_schedule
    - action_student_schedule
    - reset_slots
* trial_schedule{"type": "kerja praktek"}
    - slot{"type": "kerja praktek"}
    - action_trial_schedule
    - reset_slots
* lecturer_schedule{"time": "jam", "lecturer": "gerry"}
    - slot{"lecturer": "gerry"}
    - slot{"time": "jam"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
* lecturer_whatsapp_number{"lecturer": "bagus"}
    - slot{"lecturer": "bagus"}
    - action_lecturer_whatsapp_number
    - slot{"ask_lecturer_whatsapp_number": null}
* practicum_schedule{"practicum": "Sistem Digital"}
    - slot{"practicum": "Sistem Digital"}
    - action_practicum_schedule
    - reset_slots
* practicum_value{"practicum": "Pengembangan Teknologi Website", "day": "kemarin"}
    - slot{"day": "kemarin"}
    - slot{"practicum": "Pengembangan Teknologi Website"}
    - action_practicum_value
    - reset_slots
* student_schedule{"time": "sebelumnya"}
    - slot{"time": "sebelumnya"}
    - action_student_schedule
    - reset_slots
* student_schedule
    - action_student_schedule
    - reset_slots

## interactive_story_1
* lecturer_schedule{"lecturer": "erry"}
    - slot{"lecturer": "erry"}
    - action_lecturer_schedule
    - slot{"ask_lecturer_schedule": null}
