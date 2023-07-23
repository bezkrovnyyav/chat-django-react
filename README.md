---
 **Task**: 
 **1.** [ ] Користувачі можуть приєднатися, використовуючи лише ім'я користувача (авторизація не потрібна). 
 **2.** [X] Одночасно можуть спілкуватися в чаті більше 2 користувачів (навіть з однаковими псевдонімами). 
 **3.** [X] Не можна використовувати бібліотеки чатів у проекті. 
 **4.**  [X] повідомлення з’являються миттєво; 
 **5.** [X] власні повідомлення з’являються на другій відкритій вкладці; 
 **6.** [ ] екран чату має завжди прокручуватися до останнього повідомлення; 
 **7.**  [ ] користувачі мають бачити, коли хтось набирає текст; 
 **8.** [ ] відображати дату й час біля кожного повідомлення; 
 **9.** [ ] ім'я користувача залишається після вкладки, що закривається.
---
**Start project**:
---
 **1.** In the first console:
 	 `Open chat-django-react`
	 `python -m venv env`
	 `env\Scripts\activate`
	 `pip install -r requirements.txt`
    Open backend directory via `--> cd backend` 
    `python manage.py migrate `
   `python manage.py makemigrations `
   `python manage.py runserver`
   For create admin --> `python manage.py createsuperuser`
---
**2.** In the second console:
 - Open frontend directory via `--> cd frontend` 
 - `npm install` 
 - `npm start` 

 **3.** Open the app  --> `http://localhost:3000`