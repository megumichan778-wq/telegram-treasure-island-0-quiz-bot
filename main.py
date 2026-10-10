import logging
from telegram import Update, Poll
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ---------------------------------------------------------
# :8919176187:AAH-sd7TmnVy_mwyKabDXaTQf2wcmB44L3g
# ---------------------------------------------------------
TOKEN = "8919176187:AAH-sd7TmnVy_mwyKabDXaTQf2wcmB44L3g"

# ---------------------------------------------------------
# 100 پرسیارەکەی بەشی یەکەم (Chapter 1)
# ---------------------------------------------------------
QUIZ_DATA = [
    {
        "question": "1. Who is the narrator of Treasure Island?",
        "options": ["Dr. Livesey", "Jim Hawkins", "Squire Trelawney", "Billy Bones"],
        "correct_option_id": 1,
        "explanation": "Jim Hawkins narrates the story in first-person."
    },
    {
        "question": "2. Why is Jim Hawkins writing the story?",
        "options": ["To earn money", "Because Dr. Livesey and Squire Trelawney asked him to", "To make a map", "Because he wants to become a pirate"],
        "correct_option_id": 1,
        "explanation": "Dr. Livesey and Squire Trelawney asked Jim to write down all particulars."
    },
    {
        "question": "3. What is the name of the inn where Jim's family lived?",
        "options": ["The Spy-glass Inn", "The Hispaniola", "The Admiral Benbow", "The Golden Hind"],
        "correct_option_id": 2,
        "explanation": "The inn was called The Admiral Benbow."
    },
    {
        "question": "4. What did the old seaman ask people to call him?",
        "options": ["Billy", "Captain", "Sir", "Matey"],
        "correct_option_id": 1,
        "explanation": "He demanded people to call him Captain."
    },
    {
        "question": "5. How did the old seaman arrive at the inn?",
        "options": ["On a horse", "In a carriage, dragging a chest", "Walking, followed by a handbarrow with his sea-chest", "By boat"],
        "correct_option_id": 2,
        "explanation": "He arrived walking, followed by a handbarrow carrying his sea-chest."
    },
    {
        "question": "6. What physical feature was prominent on the old seaman’s cheek?",
        "options": ["A large mole", "A saber cut / scar", "A tattoo", "A burn mark"],
        "correct_option_id": 1,
        "explanation": "He had a livid white saber cut across his cheek."
    },
    {
        "question": "7. What was inside the sea-chest that the captain brought?",
        "options": ["Food", "Books", "Clothes and private items (locked)", "Gold coins"],
        "correct_option_id": 2,
        "explanation": "It contained his locked personal items and clothes."
    },
    {
        "question": "8. What song did the captain sing continually?",
        "options": ["Rule, Britannia!", "Fifteen Men on the Dead Man's Chest", "A Sailor's Life", "Over the Sea to Skye"],
        "correct_option_id": 1,
        "explanation": "His constant song was 'Fifteen Men on the Dead Man's Chest'."
    },
    {
        "question": "9. What job did the captain give to Jim Hawkins?",
        "options": ["To wash his clothes", "To watch out for a seafaring man with one leg", "To serve him food", "To clean his cutlass"],
        "correct_option_id": 1,
        "explanation": "Jim was paid to keep an eye out for a one-legged seafaring man."
    },
    {
        "question": "10. How much did the captain pay Jim every month for his task?",
        "options": ["One golden guinea", "Fourpence", "One silver shilling", "Sixpence"],
        "correct_option_id": 1,
        "explanation": "He promised him a four-penny piece monthly."
    },
    {
        "question": "11. What kind of person was the captain when he was drunk?",
        "options": ["Quiet and shy", "Violent, loud, and demanding", "Generous and cheerful", "Sleepy"],
        "correct_option_id": 1,
        "explanation": "He became violent, loud, and terrorized everyone."
    },
    {
        "question": "12. How did the local people feel about the captain?",
        "options": ["They loved him", "They were terrified of him", "They ignored him", "They laughed at him"],
        "correct_option_id": 1,
        "explanation": "They were terrified of his fierce temper and stories."
    },
    {
        "question": "13. Why did Dr. Livesey come to the Admiral Benbow in Chapter 1?",
        "options": ["To drink rum with the captain", "To arrest the captain", "To examine Jim's sick father", "To buy the inn"],
        "correct_option_id": 2,
        "explanation": "He came to attend to Jim's sick father."
    },
    {
        "question": "14. What dual role did Dr. Livesey hold in the community?",
        "options": ["Doctor and Magistrate (Judge)", "Doctor and Mayor", "Teacher and Doctor", "Captain and Doctor"],
        "correct_option_id": 0,
        "explanation": "He served as both medical doctor and magistrate."
    },
    {
        "question": "15. What threatened weapon did the captain pull on Dr. Livesey?",
        "options": ["A pistol", "A pocket knife", "A cutlass (clasp-knife)", "A dagger"],
        "correct_option_id": 2,
        "explanation": "He drew his cutlass / clasp-knife."
    },
    {
        "question": "16. How did Dr. Livesey react when the captain pulled his weapon?",
        "options": ["He ran away", "He drew a gun", "He stayed calm and spoke firmly to him", "He apologized"],
        "correct_option_id": 2,
        "explanation": "He remained completely calm and spoke to him without fear."
    },
    {
        "question": "17. What did Dr. Livesey warn the captain about if he continued drinking rum?",
        "options": ["He would go blind", "He would die of a stroke", "He would be hanged by the law", "Both B and C"],
        "correct_option_id": 3,
        "explanation": "He warned him about health risks and being hanged by law."
    },
    {
        "question": "18. What was the health condition of Jim's father in Chapter 1?",
        "options": ["Healthy and strong", "Very sick and weak", "Blind", "Injured in a fight"],
        "correct_option_id": 1,
        "explanation": "He was very sick and eventually passed away."
    },
    {
        "question": "19. What instrument did the captain use to look out at the sea?",
        "options": ["A microscope", "A brass telescope", "A pair of spectacles", "A compass"],
        "correct_option_id": 1,
        "explanation": "He used a brass telescope."
    },
    {
        "question": "20. What did the captain usually eat for breakfast?",
        "options": ["Bread and milk", "Bacon and eggs", "Fish", "Eggs and toast with rum"],
        "correct_option_id": 3,
        "explanation": "He drank rum and ate heartily."
    },
    {
        "question": "21. Where did the story of Chapter 1 take place geographically?",
        "options": ["London", "Near Black Hill Cove in England", "Bristol", "Jamaica"],
        "correct_option_id": 1,
        "explanation": "Near Black Hill Cove in England."
    },
    {
        "question": "22. Why did the captain keep to himself during the day?",
        "options": ["He was sleeping", "He was looking out for unwanted visitors/pirates", "He was writing a diary", "He was fishing"],
        "correct_option_id": 1,
        "explanation": "He scanned the horizon for enemies or anyone he feared."
    },
    {
        "question": "23. Who was the only person who stood up to the captain’s bad behavior?",
        "options": ["Jim", "Jim's mother", "Dr. Livesey", "Jim's father"],
        "correct_option_id": 2,
        "explanation": "Dr. Livesey stood up to him bravely."
    },
    {
        "question": "24. How did Jim feel about the 'one-legged seafaring man'?",
        "options": ["He wasn't bothered", "He had terrible nightmares about him", "He was excited to meet him", "He thought he was a myth"],
        "correct_option_id": 1,
        "explanation": "He suffered from terrible nightmares about him."
    },
    {
        "question": "25. What was the captain's real name revealed later in the chapter?",
        "options": ["Black Dog", "Billy Bones", "Long John Silver", "Flint"],
        "correct_option_id": 1,
        "explanation": "His name was Billy Bones."
    },
    {
        "question": "26. Did the captain pay his bill at the inn regularly?",
        "options": ["Yes, always in gold", "No, he stayed long past his payment and Jim's father was too afraid to ask", "He worked instead of paying", "He paid double"],
        "correct_option_id": 1,
        "explanation": "He owed money, but they were too afraid to ask."
    },
    {
        "question": "27. What did the captain do when anyone asked him questions about his past?",
        "options": ["He answered kindly", "He blew air through his nose and glared", "He cried", "He left the room"],
        "correct_option_id": 1,
        "explanation": "He blew through his nose like a fog-horn and glared."
    },
    {
        "question": "28. What kind of stories did the captain tell at night?",
        "options": ["Fairy tales", "Scary stories about hanging, storms, and sea-faring crimes", "Love stories", "Stories about family"],
        "correct_option_id": 1,
        "explanation": "Terrifying stories of storms, hangings, and wicked deeds."
    },
    {
        "question": "29. How did Dr. Livesey describe the captain when he confronted him?",
        "options": ["A brave warrior", "A dirty, drunken scoundrel", "A noble gentleman", "A poor sick man"],
        "correct_option_id": 1,
        "explanation": "He called him a dirty, drunken scoundrel."
    },
    {
        "question": "30. What was the effect of rum on the captain’s health?",
        "options": ["It made him stronger", "It caused him serious health risks (stroke)", "It cured his illness", "It had no effect"],
        "correct_option_id": 1,
        "explanation": "It severely damaged his health."
    },
    {
        "question": "31. Who stayed at the inn during the cold winter?",
        "options": ["Many tourists", "The old captain remained as the only long-term guest", "Squire Trelawney", "Soldiers"],
        "correct_option_id": 1,
        "explanation": "The captain was the sole long-term guest."
    },
    {
        "question": "32. What made the captain's appearance look rough?",
        "options": ["His dirty pigtail and soil on his coat", "His expensive clothes", "His shiny armor", "His clean uniform"],
        "correct_option_id": 0,
        "explanation": "His stained coat and untidy appearance."
    },
    {
        "question": "33. What did Dr. Livesey mean by calling himself a 'magistrate'?",
        "options": ["He was a sailor", "He was an officer of the law / judge", "He was a merchant", "He was a teacher"],
        "correct_option_id": 1,
        "explanation": "He held judicial power as a justice of the peace."
    },
    {
        "question": "34. How did Jim's father die?",
        "options": ["Killed by pirates", "Drowned in the sea", "Died of a severe illness", "Shot in a duel"],
        "correct_option_id": 2,
        "explanation": "He died of his illness."
    },
    {
        "question": "35. What season was it when the events of Chapter 1 occurred?",
        "options": ["Mid-summer", "A bitterly cold winter", "Late spring", "Early autumn"],
        "correct_option_id": 1,
        "explanation": "It happened during a harsh winter."
    },
    {
        "question": "36. Why didn't Jim’s father demand money from the captain?",
        "options": ["He was rich", "He was too afraid of the captain's temper", "The captain was his brother", "The inn was free"],
        "correct_option_id": 1,
        "explanation": "Fear of the captain's ferocious temper."
    },
    {
        "question": "37. What was the overall tone of Chapter 1?",
        "options": ["Funny and romantic", "Mysterious, tense, and suspenseful", "Sad and boring", "Historical"],
        "correct_option_id": 1,
        "explanation": "It sets a mysterious and tense atmosphere."
    },
    {
        "question": "38. The captain's song 'Dead Man's Chest' refers to:",
        "options": ["A real treasure chest", "An island / rock named Dead Man's Chest", "A coffin", "A ship"],
        "correct_option_id": 1,
        "explanation": "It refers to an actual island in the Caribbean."
    },
    {
        "question": "39. What did the captain do every evening by the fire?",
        "options": ["Read books", "Drink rum and force people to listen to his stories", "Sleep on the floor", "Play cards"],
        "correct_option_id": 1,
        "explanation": "Drank rum and terrified listeners with stories."
    },
    {
        "question": "40. Who was the first person to break the captain's dominance in the inn?",
        "options": ["Jim Hawkins", "Dr. Livesey", "Jim's mother", "Squire Trelawney"],
        "correct_option_id": 1,
        "explanation": "Dr. Livesey successfully defied him."
    },
    {
        "question": "41. Why did Jim’s mother worry about the captain?",
        "options": ["He didn't eat enough", "His presence and bad reputation might ruin the inn's business", "He was too noisy", "Both B and C"],
        "correct_option_id": 3,
        "explanation": "She feared he would ruin business and not pay."
    },
    {
        "question": "42. How did Jim describe the captain's hands?",
        "options": ["Clean and soft", "Ragged, scarred, with black broken nails", "Small and delicate", "Covered in rings"],
        "correct_option_id": 1,
        "explanation": "Broken, black nails and scarred hands."
    },
    {
        "question": "43. What was the captain holding in his hand when he first arrived?",
        "options": ["A gun", "A wooden stick (handbarrow reference)", "A brass telescope", "A bottle of wine"],
        "correct_option_id": 2,
        "explanation": "He carried his telescope."
    },
    {
        "question": "44. What did Dr. Livesey promise to do if the captain misbehaved again?",
        "options": ["Throw him in the sea", "Have him tracked and hanged by law", "Shoot him", "Close the inn"],
        "correct_option_id": 1,
        "explanation": "Promised to have him hanged by the law."
    },
    {
        "question": "45. The 'one-legged man' was someone Billy Bones was:",
        "options": ["Looking for as a friend", "Terrified of meeting", "Planning to employ", "Related to"],
        "correct_option_id": 1,
        "explanation": "He was terrified of him."
    },
    {
        "question": "46. What type of knife did Billy Bones carry?",
        "options": ["A small penknife", "A clasp-knife (cutlass style)", "A sword", "A spear"],
        "correct_option_id": 1,
        "explanation": "A clasp-knife."
    },
    {
        "question": "47. What did Jim Hawkins do when he saw the one-legged man in his dreams?",
        "options": ["Woke up laughing", "Woke up in a cold sweat of terror", "Slept peacefully", "Forgot about it"],
        "correct_option_id": 1,
        "explanation": "Woke up terrified."
    },
    {
        "question": "48. What was the full title of Chapter 1?",
        "options": ["The Sea-Chest", "The Old Sea-dog at the Admiral Benbow", "The Black Spot", "Long John Silver"],
        "correct_option_id": 1,
        "explanation": "The Old Sea-dog at the Admiral Benbow."
    },
    {
        "question": "49. Who wrote the novel Treasure Island?",
        "options": ["Charles Dickens", "Robert Louis Stevenson", "William Shakespeare", "Mark Twain"],
        "correct_option_id": 1,
        "explanation": "Robert Louis Stevenson."
    },
    {
        "question": "50. What point of view is Chapter 1 written in?",
        "options": ["Third-person limited", "First-person (Jim Hawkins)", "Second-person", "Omniscient"],
        "correct_option_id": 1,
        "explanation": "First-person narrative by Jim."
    },
    {
        "question": "51. Jim Hawkins tells the story years after the event. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True, he writes it as a memoir later."
    },
    {
        "question": "52. The old captain was polite and quiet. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, he was loud and rude."
    },
    {
        "question": "53. Jim was paid fourpence a month to watch for a one-legged man. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "54. Dr. Livesey was afraid of the captain's knife. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, he remained fearless."
    },
    {
        "question": "55. Jim's father was healthy in Chapter 1. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, he was gravely ill."
    },
    {
        "question": "56. The inn's name was The Admiral Benbow. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "57. The captain's chest was left unlocked. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, it was heavily locked."
    },
    {
        "question": "58. Billy Bones drank large amounts of rum daily. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "59. Dr. Livesey was both a doctor and magistrate. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "60. The captain sang a cheerful song about birds. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, it was a grim pirate song."
    },
    {
        "question": "61. Townspeople were frightened by the captain. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "62. The captain stayed for free because he owned it. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, he was just a paying guest (who didn't pay)."
    },
    {
        "question": "63. Jim had nightmares about a one-legged man. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "64. Dr. Livesey threatened to have him hanged. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "65. The captain carried a brass telescope. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "66. Jim's father died before the chapter ended. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "67. The captain paid his bills punctually. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, he owed money."
    },
    {
        "question": "68. Squire Trelawney fought the captain in Chapter 1. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False."
    },
    {
        "question": "69. The captain had a saber cut on his cheek. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "70. Dr. Livesey came to arrest the captain. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False, he came to treat Jim's father."
    },
    {
        "question": "71. The captain feared a one-legged man. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "72. The setting is near the English coast. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "73. The captain loved sharing his money with everyone. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 1,
        "explanation": "False."
    },
    {
        "question": "74. Robert Louis Stevenson wrote the book. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "75. The captain caused great anxiety to Jim's father. (True/False)",
        "options": ["True", "False"],
        "correct_option_id": 0,
        "explanation": "True."
    },
    {
        "question": "76. Who is the narrator?",
        "options": ["Jim Hawkins", "Billy Bones", "Dr. Livesey", "Squire"],
        "correct_option_id": 0,
        "explanation": "Jim Hawkins."
    },
    {
        "question": "77. Name of the inn?",
        "options": ["The Admiral Benbow", "Spy-glass", "Hispaniola", "Anchor"],
        "correct_option_id": 0,
        "explanation": "The Admiral Benbow."
    },
    {
        "question": "78. What was on the captain's face?",
        "options": ["A saber cut", "A tattoo", "A beard", "A mole"],
        "correct_option_id": 0,
        "explanation": "A saber cut."
    },
    {
        "question": "79. What song did he sing?",
        "options": ["Fifteen Men on the Dead Man's Chest", "Rule Britannia", "Home Sweet Home", "Sea Shanties"],
        "correct_option_id": 0,
        "explanation": "Fifteen Men on the Dead Man's Chest."
    },
    {
        "question": "80. How much was Jim paid monthly?",
        "options": ["Fourpence", "One shilling", "A guinea", "Ten pence"],
        "correct_option_id": 0,
        "explanation": "Fourpence."
    },
    {
        "question": "81. Who was the captain afraid of?",
        "options": ["A one-legged sailor", "Black Dog", "Dr. Livesey", "The King"],
        "correct_option_id": 0,
        "explanation": "A one-legged sailor."
    },
    {
        "question": "82. Why did Dr. Livesey visit?",
        "options": ["To see Jim's sick father", "To drink", "To buy land", "To meet pirates"],
        "correct_option_id": 0,
        "explanation": "To see Jim's sick father."
    },
    {
        "question": "83. Dr. Livesey's extra profession?",
        "options": ["Magistrate", "Teacher", "Captain", "Merchant"],
        "correct_option_id": 0,
        "explanation": "Magistrate."
    },
    {
        "question": "84. Weapon drawn by the captain?",
        "options": ["Cutlass", "Pistol", "Sword", "Spear"],
        "correct_option_id": 0,
        "explanation": "Cutlass / clasp-knife."
    },
    {
        "question": "85. Doctor's reaction to the threat?",
        "options": ["Calm and firm", "Scared", "Ran away", "Fought back"],
        "correct_option_id": 0,
        "explanation": "Calm and firm."
    },
    {
        "question": "86. Doctor's warning to him?",
        "options": ["Death by rum or hanging", "Go to prison", "Leave the country", "Stop singing"],
        "correct_option_id": 0,
        "explanation": "Death by rum or hanging by law."
    },
    {
        "question": "87. What heavy item did he bring?",
        "options": ["A sea-chest", "A barrel", "A safe", "A large bag"],
        "correct_option_id": 0,
        "explanation": "A heavy sea-chest."
    },
    {
        "question": "88. Why didn't Jim's father ask for rent?",
        "options": ["Too terrified", "He was rich", "Paid in advance", "Friends"],
        "correct_option_id": 0,
        "explanation": "Too terrified."
    },
    {
        "question": "89. Tool used to watch the sea?",
        "options": ["Brass telescope", "Binoculars", "Microscope", "Magnifier"],
        "correct_option_id": 0,
        "explanation": "Brass telescope."
    },
    {
        "question": "90. Effect on townspeople?",
        "options": ["Frightened", "Happy", "Indifferent", "Amused"],
        "correct_option_id": 0,
        "explanation": "Frightened."
    },
    {
        "question": "91. Type of stories told?",
        "options": ["Scary pirate and crime tales", "Fairy tales", "Romantic stories", "True history"],
        "correct_option_id": 0,
        "explanation": "Scary stories."
    },
    {
        "question": "92. Who asked Jim to write the memoirs?",
        "options": ["Dr. Livesey and Squire Trelawney", "His mother", "The captain", "His friends"],
        "correct_option_id": 0,
        "explanation": "Dr. Livesey and Squire Trelawney."
    },
    {
        "question": "93. Condition of Jim's father?",
        "options": ["Gravely ill", "Healthy", "Traveling", "Working"],
        "correct_option_id": 0,
        "explanation": "Gravely ill."
    },
    {
        "question": "94. Season during the chapter?",
        "options": ["Winter", "Summer", "Spring", "Autumn"],
        "correct_option_id": 0,
        "explanation": "Winter."
    },
    {
        "question": "95. Real name of the captain?",
        "options": ["Billy Bones", "John Silver", "Captain Flint", "Black Dog"],
        "correct_option_id": 0,
        "explanation": "Billy Bones."
    },
    {
        "question": "96. Reaction to personal questions?",
        "options": ["Blew through nose and glared", "Answered politely", "Cried", "Smiled"],
        "correct_option_id": 0,
        "explanation": "Blew through nose and glared."
    },
    {
        "question": "97. Mother's worry?",
        "options": ["Ruining business and no rent", "His health", "Food shortage", "Weather"],
        "correct_option_id": 0,
        "explanation": "Ruining business and no rent."
    },
    {
        "question": "98. Jim's nightmares about?",
        "options": ["One-legged man", "Storms", "Ghosts", "The doctor"],
        "correct_option_id": 0,
        "explanation": "One-legged man."
    },
    {
        "question": "99. Author of the novel?",
        "options": ["Robert Louis Stevenson", "Charles Dickens", "Mark Twain", "J.K. Rowling"],
        "correct_option_id": 0,
        "explanation": "Robert Louis Stevenson."
    },
    {
        "question": "100. Main setting of Chapter 1?",
        "options": ["Admiral Benbow Inn", "On a ship", "An island", "London"],
        "correct_option_id": 0,
        "explanation": "Admiral Benbow Inn."
    }
]

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ---------------------------------------------------------
# سیستەمی ناردنی پرسیارەکان بە پۆل (Poll Quiz)
# ---------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"سڵاو {user_name}!\n\n"
        "بەخێربێیت بۆ بۆتی تاقیکردنەوەی وزاری **Treasure Island - Chapter 1**.\n"
        "ئەم بۆتە ١٠٠ پرسیاری هەمەلایەنەی تێدایە.\n"
        "بۆ دەستپێکردنی تاقیکردنەوەکە، فەرمانی /quiz بنێرە."
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def send_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ناردنی یەکەم پرسیار
    context.user_data["current_question"] = 0
    await send_next_question(update, context)

async def send_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    index = context.user_data.get("current_question", 0)
    
    if index < len(QUIZ_DATA):
        q = QUIZ_DATA[index]
        chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat_id
        
        await context.bot.send_poll(
            chat_id=chat_id,
            question=q["question"],
            options=q["options"],
            type=Poll.QUIZ,
            correct_option_id=q["correct_option_id"],
            explanation=q["explanation"],
            is_anonymous=False
        )
        context.user_data["current_question"] = index + 1
        
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"بۆ بینینی پرسیاری داهاتوو ({context.user_data['current_question']}/100)، تکایە فەرمانی /next بنێرە."
        )
    else:
        chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat_id
        await context.bot.send_message(
            chat_id=chat_id,
            text="دەستخۆش! تۆ هەموو ١٠٠ پرسیارەکەی ئەم بەشەت بەسەرکەوتوویی تەواو کرد.\nبۆ دووبارەکردنەوەی تاقیکردنەوەکە بنووسە /quiz"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", send_quiz))
    app.add_handler(CommandHandler("next", send_next_question))

    print("Bot with 100 questions is running successfully...")
    app.run_polling()

if __name__ == "__main__":
    main()
