TOKEN = '7072533425:AAGBQHvd-HX5Dc8gosjOMp7A4VtZ6A4RS6M'
TOKEN_VK = 'YOU TOKEN VK'


'''Настройка отправки результата тестирования по эл. почте'''
from_email = 'korminkms@mail.ru'
passw_external_app = 'Пароль для внешнего приложения'
'''для mail.ru - https://help.mail.ru/mail/security/protection/external/
   для yandex.ru - https://yandex.ru/support/id/authorization/app-passwords.html'''


'''Вопросы к викторине'''
dict_questions = {
    1: {'Ваше лучшее качество?':
            [['Смелость', 50],
             ['Ум', 60],
             ['Доброта', 30],
             ['Артистичность', 20],
             ['Честность', 10],
             ['Обаяние', 40]]},

    2: {'Какую музыку вы слушаете?':
            [['Поп, легкая', 30],
             ['Рок, металл', 50],
             ['Классика', 10],
             ['Разные стили, но с красивым вокалом', 40],
             ['Инструментальная', 60],
             ['Я не слушаю, я пишу музыку', 20]]},

    3: {'Ваше отрицательное качество?':
            [['Медлительность', 60],
             ['Застенчивость', 10],
             ['Капризность', 20],
             ['Своеволие', 40],
             ['Излишняя придирчивость', 50],
             ['Не умение говорить «нет»', 30]]},

    4: {'Что является важным в жизни?':
            [['Семья, дети', 10],
             ['Здоровье', 40],
             ['Творчество', 20],
             ['Карьера', 60],
             ['Свобода', 50],
             ['Любовь', 30]]},

    5: {'Что вы любите?':
            [['Приключения, страсть, азарт, мегаполис', 20],
             ['Друзья, общение, дискуссии, поззия', 30],
             ['Веселье, теплая погода, ритм, красота', 40],
             ['Дети, полевые цветы; запах выпечки', 10],
             ['Ветер, ночь, скорость, шум дорог', 50],
             ['Антиквариат, размышления, шорох листьев', 60]]},

    6: {'Что вы ненавидите?':
            [['Ложь, пустые обещания', 30],
             ['Когда торопят, рисковать', 60],
             ['Ограничения разного рода', 40],
             ['Грусть, одиночество', 20],
             ['Зависть, дисциплину', 50],
             ['Глупых людей', 10]]},

    7: {'Ваше любимое занятие?':
            [['Танцевать, участвовать в постановках', 20],
             ['Чтение и шахматы', 60],
             ['Рисование, рукоделие', 40],
             ['Турпоходы, путешествия', 50],
             ['Кулинария, цветы, садоводство', 10],
             ['Музыка, кино, дизайн', 30]]},

    8: {'Ваша мечта?':
            [['Объехать весь мир', 50],
             ['Слава и успех', 20],
             ['Жить полной жизнью', 40],
             ['Мир во всем мире', 30],
             ['Как у всех: дом, семья…', 10],
             ['Стать профессионалом в каком-то деле', 60]]},

    9: {'Выберите фразу:':
            [['Мы живем сегодняшним днем', 40],
             ['Главное стремление человека выжить', 10],
             ['Любовь спасет мир', 30],
             ['Верь в мечту, и все сбудется!', 50],
             ['Движение это жизнь', 20],
             ['Будь великодушным, ты сделан из звезд', 60]]},

    10: {'На что вы обращаете внимание при знакомстве счеловеком?':
             [['Взгляд, глаза', 50],
              ['Движение, мимика', 10],
              ['Губы, улыбка', 30],
              ['Внешность в целом', 40],
              ['Запах, парфюм', 20],
              ['Речь, голос', 60]]}
}

'''Результаты викторины
Результаты теста выводятся в формате parse_mode="Markdown". Используйте * - для выделения текста жирным шрифтом '''

quize_result = {1: [[100, 170], '🐸 Ваше тотемное животное – *ЛЯГУШКА*. \
Это талисман для доброго, скромного и домашнего человека. Лягушка будет защищать ваш дом, сохранит хозяйство. \
Талисман поможет найти истинную любовь и отличать настоящих друзей от фальшивых. \
Если хотите гармоничной и благополучной жизни, приобретите фигурку лягушки.', 'frog.jpg'],
                2: [[180, 260], '🦌 Ваше тотемное животное – *АНТИЛОПА*. \
Этот талисман для красивой и творческой личности, помогает сохранить красоту, подарит особую пластичность и грацию. \
Поэтому он особенно хорош для тех, кто занимается танцами и балетом. \
Фигурка этого прекрасного животного ещё поможет и сохранить любовь.', 'antelope.jpg'],
                3: [[270, 350], '🐬 Ваше тотемное животное – *ДЕЛЬФИН*. \
Вы такой же добрый, открытый и общительный, как и ваш морской покровитель. Приобретите талисман дельфина. \
Он принесет вам счастье, настоящую любовь и верных друзей. Если отправляетесь в морской круиз, возьмите фигурку с собой. \
Она защищает от шторма и катастроф.', 'delfin.jpg'],
                4: [[360, 440], '🐈 Ваше тотемное животное – *КОШКА*. \
Этот талисман подойдет яркому и независимому человеку. Он поможет добиться поставленной цели, исполнить желание, \
привлечь любовь, сохранить семью. Вообще у этого талисмана практически нет недостатков. Отдельно о девушках. \
Этот талисман поможет сохранить молодость и красоту на многие годы.', 'cat.jpg'],
                5: [[450, 520], '🐺 Ваше тотемное животное – *ВОЛК*. \
Вы представитель редкого типа людей. Больше всего на свете цените свободу и независимость. \
Настоящих друзей у вас немного, вы комфортно чувствуете себя и в одиночестве. Носите одежду с изображением волка и \
приобретите сувенир. Он поможет раскрыться таким качеством, как смелость, упорство, мужество.', 'wolf.jpg'],
                6: [[530, 600], '🐘 Ваше тотемное животное — *СЛОН*. \
Вы, как и ваш покровитель, мудрый, спокойный и рассудительный человек. \
Вы никогда никуда не торопитесь, среди знакомых словёте интеллектуалом. Талисман слона поможет добиться успеха в карьере, \
подарит благополучие и счастье. Также он незаменим, если вы занимаетесь наукой, помогает сохранить ясный ум и силу духа.',
                    'elephant.jpg']}

'''Результаты тестирования по дю рождения'''

dict_date_of_birth = {'10 декабря - 09 января': ['🐻 Ваше тотемное животное - *Медведь*. Онолицетворять такие качества, как сила, мощь и защита. \
Медведи известны своей физической силой, способностью выживать в суровых условиях и защищать свою территорию. \
Если ваше тотемное животное медведь, то возможно вы обладаете этими качествами и способны преодолевать трудности и \
защищать свои интересы. Также, возможно, вы цените семью и друзей и готовы защищать их любой ценой, как и медведи, \
которые образуют сильные социальные группы и защищают свою территорию и членов стаи.', 'bear.jpg'],
                      '10 января - 09 февраля': ['🦦 Ваше тотемное животное - *Росомаха*. Она олицетворяет такие качества, как стойкость, \
независимость и агрессия. Россомахи известны своей способностью выживать в самых суровых условиях и защищать свою территорию. \
Если ваше тотемное животное россомаха, то возможно вы обладаете этими качествами и способны преодолевать трудности и \
защищать свои интересы. Также, возможно, вы цените свободу и независимость, как и россомахи, которые предпочитают жить в \
одиночку или небольшими группами.', 'wolverine.jpg'],
                      '10 февраля - 09 марта': ['🪶 Ваше тотемное животное - *Ворон*. Он олицетворяет такие качества, как интеллект, таинственность и долголетие. \
Вороны известны своей интеллектуальной способностью и долгой продолжительностью жизни. Если ваше тотемное животное ворон, \
то возможно вы обладаете этими качествами и способны мыслить глубоко и аналитически. Также, возможно, \
вы цените таинственность и магию, как и вороны, которые иногда ассоциируются с оккультными знаниями и мистикой.',
                                                'raven.jpg'],
                      '10 марта - 09 апреля': ['🦦 Ваше тотемное животное - *Горностай*. Он олицетворяет такие качества, как чистота, благородство и ловкость. \
Горностаи известны своей белой зимней шерстью, которая символизирует чистоту, и своей способностью быстро передвигаться \
и ловко охотиться. Если ваше тотемное животное горностай, то возможно вы обладаете этими качествами и стремитесь к чистоте \
и благородству в своих мыслях и действиях. Также, возможно, вы цените ловкость и быстроту в решении задач и преодолении \
препятствий, как и горностаи, которые известны своей быстротой и ловкостью.', 'ermine.jpg'],
                      '10 апреля - 09 мая': ['🐸 Ваше тотемное животное - *Жаба*. Она олицетворяет такие качества, как трансформация, возрождение и очищение. \
Жабы известны своей способностью проходить через стадии метаморфозы и возрождаться в новой форме. \
Если ваше тотемное животное жаба, то возможно вы обладаете этими качествами и способны к глубоким внутренним преобразованиям \
и личностному росту. Также, возможно, вы цените чистоту и гармонию в окружающей среде и стремитесь поддерживать баланс и \
равновесие в своей жизни, как и жабы, которые часто ассоциируются с элементом воды и символизируют очищение и обновление.',
                                          'frog_big.jpg'],
                      '10 мая - 09 июня': ['🦗 Ваше тотемное животное - *Кузнечик*. Он олицетворяет такие качества, как адаптация, гибкость и \
чувствительность. Кузнечики известны своей способностью быстро менять свое поведение и привычки в зависимости от окружающей \
среды. Если ваше тотемное животное кузнечик, то возможно вы обладаете этими качествами и способны быстро адаптироваться к \
новым ситуациям и изменениям в жизни. Также, возможно, вы цените гармонию и баланс в окружающей среде и стремитесь сохранять \
эти качества в своей жизни, как и кузнечики, которые являются важной частью экосистемы и помогают поддерживать ее равновесие.',
                                           'grasshopper.jpg'],
                      '10 июня - 09 июля': ['🐹 Ваше тотемное животное - *Хомяк*. Он олицетворяет такие качества, как запасливость, домовитость и \
семейственность. Хомяки известны своей способностью собирать и хранить пищу, обустраивать свои жилища и заботиться о \
своем потомстве. Если ваше тотемное животное хомяк, то возможно вы обладаете этими качествами и способны организовывать \
свою жизнь, создавать уют и заботиться о близких людях. Также, возможно, вы цените стабильность и комфорт в своей жизни, \
как и хомяки, которые стремятся создать безопасную и удобную среду для себя и своей семьи.', 'hamster.jpg'],
                      '10 июля - 09 августа': ['🐌 Ваше тотемное животное - *Улитка*. Она олицетворяет такие качества, как терпение, уединение и самозащита. \
Улитки известны своей способностью медленно, но уверенно двигаться к своей цели и защищать себя с помощью своего дома-раковины. \
Если ваше тотемное животное улитка, то возможно вы обладаете этими качествами и способны терпеливо и настойчиво добиваться \
своих целей, а также находить способы защиты и самосохранения. Также, возможно, вы цените уединение и спокойствие, \
как и улитки, которые проводят большую часть времени в своем доме-раковине.', 'snail.jpg'],
                      '10 августа - 09 сентября': ['🐜 Ваше тотемное животное - *Муравей*. Он олицетворяет такие качества, как трудолюбие, \
организация и коллективная работа. Муравьи известны своей способностью строить сложные муравейники, \
заниматься сельским хозяйством и воевать с другими колониями. Если ваше тотемное животное муравей, \
то возможно вы обладаете этими качествами и способны эффективно организовывать работу, сотрудничать с другими людьми и \
достигать общих целей. Также, возможно, вы цените порядок и дисциплину, как и муравьи, которые строго следуют иерархии \
и правилам своей колонии.', 'ant.jpg'],
                      '10 сентября - 09 октября': ['🪶 Ваше тотемное животное - *Сорока*. Она олицетворяет такие качества, как общение, любопытство и активность. \
Сороки известны своей социальной природой и любовью к общению друг с другом. Если ваше тотемное животное сорока, \
то возможно вы обладаете этими качествами и любите общаться с людьми и делиться информацией. Также, возможно, \
вы любознательны и всегда ищете новую информацию, как и сороки, которые известны своим любопытством и \
исследовательским поведением.', 'magpie.jpg'],
                      '10 октября - 09 ноября': ['🦫 Ваше тотемное животное - *Бобер*. Он олицетворяет такие качества, как трудолюбие, организация и строительство. \
Бобры известны своими уникальными навыками строительства плотин и хаток. Если ваше тотемное животное бобер, \
то возможно вы обладаете организационными способностями и умеете планировать свои действия для достижения целей. \
Также, возможно, вы цените труд и умеете работать усердно, как и бобры, которые проводят большую часть своего времени \
на строительстве и поддержании своих сооружений.', 'beaver.jpg'],
                      '10 ноября - 09 декабря': ['🐶 Ваше тотемное животное - *Собака*. Она олицетворяет такие качества, как верность, преданность \
и интуиция. Собаки известны своей способностью формировать тесные связи с людьми и быть преданными своим хозяевам. \
Если ваше тотемное животное собака, то возможно вы обладаете этими качествами и способны быть верным и преданным другом. \
Также, возможно, вы цените честность и открытость в отношениях с другими людьми, как и собаки, которые обычно прямо \
выражают свои чувства и эмоции.', 'dog.jpg']
                      }

'''Описание программы 'Программа *«Возьми животное под опеку»*'''
about_prog = '🐳 Программа *«Возьми животное под опеку»* дает возможность опекунам ощутить свою причастность \
к делу сохранения природы, участвовать в жизни Московского зоопарка и его обитателей, \
видеть конкретные результаты своей деятельности. Опекать – значит помогать любимым животным. \
*Опека* — это прекрасная возможность принять участие в деле сохранения редких видов, \
помочь нам в реализации природоохранных программ.\n\n\
💰 Стоимость опеки рассчитывается из ежедневного рациона питания животного. \n\n\
Если вы уже выбрали животное и хотите узнать стоимость опеки над ним, вам нужно отправить \
свой запрос на почту, позвонить по телефонам или оставить заявку на сайте.\n\n\
*Наши Контакты*👇\n\
+7(962)9713875 c 9:00 до 18:00\n\
zoofriends@moscowzoo.ru'


'''Приветственное сообщение бота'''
intro = '👉 Участвуйте в программе *«Возьми животное под опеку»* — это ваш личный вклад \
в дело сохранения биоразнообразия Земли и развитие нашего зоопарка.\n\n\
Но для начала узнайте своё тотемное животное. \n\n\
🐒 *Тотемное животное* - это символ, связанный с магическими верованиями и традициями некоторых культур. \
Оно представляет собой не само животное, а заключенную в нем безличную магическую субстанцию, которая может влиять \
на судьбу человека. Тотемное животное может быть представлено в образе животного и часто ассоциируется с личными качествами,\
с днем или годом рождения. 👇'


'''Intro к тесту по году рождения'''
intro_zoroastri = '📢 Одна из самых древних мировых религий — это *зороастризм*. Мифология зороастризма используется \
в основе создания многих тотемных гороскопов, самый известный из которых 32-цикличный зороастрийский гороскоп.\
Он основывается на *32-летнем цикле Сатурна*, — планеты, которая в астрологии символизирует внутренний стержень. \
Вот почему именно этот гороскоп отражает истинную суть человека, самую сердцевину его личности.\n\n\
*Важно знать, что каждый тотемный год начинается 21 марта, в минуту первого восхода Солнца в знаке Овна. \
То есть тем, кто родился с 1 января по 20 марта, покровительствуют тотемы предыдущего года.*'


'Результаты тестирования по году рождения'
dict_zoroastri = {
    '1906': ['🦌 Ваше тотемное животное - *Олень*. Он символизирует ловкость, скорость и грацию. \
Олень также ассоциируется с новой жизнью и возрождением, поскольку каждый год он сбрасывает свои рога и отращивает новые. \
Если ваше тотемное животное олень, то возможно вы обладаете качествами, такими как быстрота, гибкость и способность \
адаптироваться к изменяющимся обстоятельствам. Также, возможно, вы цените свободу и независимость, как и олени, которые \
предпочитают жить в одиночку или небольшими ', 'deer.jpg'],
    '1907': ['🐏 Ваше тотемное животное - *Баран*. Он олицетворяет такие качества, как упорство, настойчивость и силу воли. \
Бараны известны своей способностью преодолевать препятствия и двигаться вперед, несмотря на трудности. \
Если ваше тотемное животное баран, то вероятно вы обладаете этими качествами и способны добиваться своих целей, \
даже если путь к ним труден и тернист. Однако стоит помнить, что чрезмерная упрямость и негибкость могут стать недостатками, \
поэтому важно сохранять баланс и умение приспосабливаться к изменяющимся обстоятельствам.', 'ram.jpg'],
    '1908': ['🐾 Ваше тотемное животное - *Мангуст*. Его олицетворяют такие качества, как быстрота, ловкость и смелость. \
Мангусты известны своей способностью быстро реагировать на опасность и эффективно защищаться от врагов. \
Если ваше тотемное животное мангуст, то возможно вы обладаете этими качествами и способны быстро принимать решения и \
действовать в сложных ситуациях. Также, возможно, вы цените свободу и независимость, как и мангусты, \
которые предпочитают жить в одиночку или небольшими группами.', 'mongoose.jpg'],
    '1909': ['🐺 Ваше тотемное животное - *Волк*. Волк олицетворяет такие качества, как сила, интеллект и преданность. \
Волки известны своими социальными навыками и способностью работать в команде. Если ваше тотемное животное волк, \
то возможно вы обладаете этими качествами и способны эффективно взаимодействовать с другими людьми. Также, возможно, \
вы цените семью и друзей и готовы защищать их любой ценой, как и волки, которые образуют сильные социальные группы \
и защищают свою территорию и членов стаи.', 'wolf.jpg'],
    '1910': ['🪶 Ваше тотемное животное - *Аист*. Он олицетворяет такие качества, как чистота, духовность и семейные ценности. \
Аисты известны своим заботливым отношением к потомству и долгожительством. Если ваше тотемное животное аист, \
то возможно вы обладаете этими качествами и цените свою семью и близких людей. Также, возможно, \
вы стремитесь к духовному развитию и гармонии с окружающим миром.', 'stork.jpg'],
    '1911': ['🕷️ Ваше тотемное животное - *Паук*. Он олицетворяет такие качества, как творчество, мудрость и интуиция. \
Пауки известны своими уникальными навыками плетения паутины и способностью ловить свою добычу. \
Если ваше тотемное животное паук, то возможно вы обладаете творческими способностями и умеете находить нестандартные \
решения в сложных ситуациях. Также, возможно, вы цените мудрость и умеете слушать свой внутренний голос, как и пауки, \
которые часто считаются символами интуиции и мудрости.', 'spider.jpg'],
    '1912': ['🐍 Ваше тотемное животное - *Уж*. Он олицетворяет такие качества, как гибкость, приспособляемость и магические способности. \
Ужи известны своей способностью избегать опасности и приспосабливаться к различным условиям среды. \
Если ваше тотемное животное уж, то возможно вы обладаете гибкостью и умением адаптироваться к изменяющимся обстоятельствам. \
Также, возможно, вы цените магию и мистику, как и ужи, которые иногда ассоциируются с волшебством и тайными знаниями.', 'grass-snake.jpg'],
    '1913': ['🦫 Ваше тотемное животное - *Бобёр*. Он олицетворяет такие качества, как трудолюбие, организация и строительство. \
Бобры известны своими уникальными навыками строительства плотин и хаток. Если ваше тотемное животное бобер, \
то возможно вы обладаете организационными способностями и умеете планировать свои действия для достижения целей. \
Также, возможно, вы цените труд и умеете работать усердно, как и бобры, которые проводят большую часть своего времени \
на строительстве и поддержании своих сооружений.', 'beaver.jpg'],
    '1914': ['🐢 Ваше тотемное животное - *Черепаха*. Она олицетворяет такие качества, как терпение, стабильность и защита. \
Черепахи известны своей прочной броней и медленным, но устойчивым движением. Если ваше тотемное животное черепаха, \
то возможно вы обладаете этими качествами и способны сохранять спокойствие и стабильность в любых обстоятельствах. \
Также, возможно, вы цените защиту и безопасность, как и черепахи, которые используют свою броню для защиты от хищников.', 'turtle.jpg'],
    '1915': ['🪶 Ваше тотемное животное - *Сорока*. Она олицетворяет такие качества, как общение, любопытство и активность. \
Сороки известны своей социальной природой и любовью к общению друг с другом. Если ваше тотемное животное сорока, \
то возможно вы обладаете этими качествами и любите общаться с людьми и делиться информацией. Также, возможно, \
вы любознательны и всегда ищете новую информацию, как и сороки, которые известны своим любопытством и \
исследовательским поведением.', 'magpie.jpg'],
    '1916': ['🐿️ Ваше тотемное животное - *Белка*. Она  олицетворяет такие качества, как ловкость, быстрота и приспособляемость. \
Белки известны своей способностью быстро перемещаться по деревьям и приспосабливаться к различным условиям среды. \
Если ваше тотемное животное белка, то возможно вы обладаете этими качествами и способны быстро адаптироваться к новым ситуациям. \
Также, возможно, вы цените активность и энергичность, как и белки, которые проводят большую часть своего времени \
в движении и поиске пищи.', 'squirrel.jpg'],
    '1917': ['🪶 Ваше тотемное животное - *Ворон*. Он олицетворяет такие качества, как интеллект, таинственность и долголетие. \
Вороны известны своей интеллектуальной способностью и долгой продолжительностью жизни. Если ваше тотемное животное ворон, \
то возможно вы обладаете этими качествами и способны мыслить глубоко и аналитически. Также, возможно, \
вы цените таинственность и магию, как и вороны, которые иногда ассоциируются с оккультными знаниями и мистикой.', 'raven.jpg'],
    '1918': ['🐓 Ваше тотемное животное - *Петух*. Он олицетворяет такие качества, как бдительность, уверенность и мужество. \
Петухи известны своими громкими криками, которые используются для предупреждения об опасности. \
Если ваше тотемное животное петух, то возможно вы обладаете этими качествами и способны быть бдительными и уверенными в себе. \
Также, возможно, вы цените мужество и готовы защищать свои убеждения и близких людей, как и петухи, \
которые известны своей храбростью и защитой своей территории.', 'cock.jpg'],
    '1919': ['🐂 Ваше тотемное животное - *Бык*. Он олицетворяет такие качества, как сила, мощь и плодородие. \
Быки известны своей физической силой и способностью обрабатывать землю. Если ваше тотемное животное бык, \
то возможно вы обладаете этими качествами и способны преодолевать трудности и достигать поставленных целей. \
Также, возможно, вы цените работу и трудолюбие, как и быки, которые проводят большую часть своего времени в \
работе и производстве продуктов.', 'bull.jpg'],
    '1920': ['🦡 Ваше тотемное животное - *Барсук*. Он олицетворяет такие качества, как упорство, настойчивость и независимость. \
Барсуки известны своей способностью рыть сложные системы нор и вести самостоятельный образ жизни. \
Если ваше тотемное животное барсук, то возможно вы обладаете этими качествами и способны преодолевать \
трудности и достигать поставленных целей. Также, возможно, вы цените независимость и предпочитаете решать \
проблемы самостоятельно, как и барсуки, которые обычно ведут одиночный образ жизни.', 'badger.jpg'],
    '1921': ['🐫 Ваше тотемное животное - *Верблюд*. Он олицетворяет такие качества, как выносливость, приспособляемость и терпение. \
Верблюды известны своей способностью переносить длительные периоды без воды и пищи, а также выживать в суровых условиях пустыни. \
Если ваше тотемное животное верблюд, то возможно вы обладаете этими качествами и способны справляться с трудностями и ждать \
благоприятных условий для достижения своих целей. Также, возможно, вы цените простоту и непритязательность, как и верблюды, \
которые не требуют особого ухода и могут выживать в самых экстремальных условиях.', 'camel.jpg'],
    '1922': ['🦔 Ваше тотемное животное - *Ёж*. Он  олицетворяет такие качества, как защита, самооборона и независимость. \
Ежи известны своей способностью сворачиваться в клубок, чтобы защитить себя от хищников. Если ваше тотемное животное ёж, \
то возможно вы обладаете этими качествами и способны защищать себя и свои границы. Также, возможно, \
вы цените независимость и предпочитаете решать проблемы самостоятельно, как и ежи, которые обычно ведут одиночный образ жизни.', 'hedgehog.jpg'],
    '1923': ['🦌 Ваше тотемное животное - *Лань*. Она олицетворяет такие качества, как грация, скорость и свобода. \
Лани известны своей быстротой и способностью легко передвигаться по пересеченной местности. \
Если ваше тотемное животное лань, то возможно вы обладаете этими качествами и стремитесь к свободе и независимости. \
Также, возможно, вы цените красоту и элегантность в окружающем мире и стараетесь привнести их в свою жизнь.', 'doe.jpg'],
    '1924': ['🐘 Ваше тотемное животное - *Слон*. Он олицетворяет такие качества, как мудрость, терпение и сила. \
Слоны известны своей долгой жизнью, умственными способностями и физической мощью. Если ваше тотемное животное слон, \
то возможно вы обладаете этими качествами и способны проявлять терпение и мудрость в принятии решений. \
Также, возможно, вы цените семью и друзей и готовы защищать их любой ценой, как и слоны, \
которые образуют сильные социальные группы и защищают свою территорию и членов стаи.', 'elephant.jpg'],
    '1925': ['🐎 Ваше тотемное животное - *Лошадь*. Она олицетворяет такие качества, как сила, свобода и дух. \
Лошади известны своей физической мощью, скоростью и независимостью. Если ваше тотемное животное лошадь, \
то возможно вы обладаете этими качествами и стремитесь к свободе и независимости. Также, возможно, вы цените дружбу и общение, \
как и лошади, которые образуют сильные социальные группы и поддерживают друг друга.', 'horse.jpg'],
    '1926': ['🐆 Ваше тотемное животное - *Гепард*. Он олицетворяет такие качества, как скорость, грация и целеустремленность. \
Гепарды известны своей невероятной быстротой и способностью охотиться на больших расстояниях. \
Если ваше тотемное животное гепард, то возможно вы обладаете этими качествами и стремитесь к достижению своих целей с \
максимальной эффективностью. Также, возможно, вы цените свободу и независимость, как и гепарды, \
которые предпочитают жить в одиночку или небольшими группами.', 'cheetah.jpg'],
    '1927': ['🦚 Ваше тотемное животное - *Павлин*. Павлин считается символом гордости и благородства. \
Это связано с его ярким и красивым внешним видом, который привлекает внимание. Если ваше тотемное животное павлин, \
то скорее всего вы обладаете такими качествами, как уверенность в себе, чувство собственного достоинства и стремление \
к прекрасному. Возможно, вы также цените красоту и элегантность в окружающем мире и стараетесь привнести их в свою жизнь.', 'peacock.jpg'],
    '1928': ['🦢 Ваше тотемное животное - *Лебедь*. Он олицетворяет такие качества, как красота, грация и верность. \
Лебеди известны своей великолепной внешностью и способностью формировать пары на всю жизнь. Если ваше тотемное животное лебедь, \
то возможно вы обладаете этими качествами и стремитесь к красоте и гармонии в своей жизни. Также, возможно, \
вы цените верность и преданность в отношениях с близкими людьми, как и лебеди, которые остаются верными своим \
партнерам до конца жизни.', 'swan.jpg'],
    '1929': ['🐈‍⬛ Ваше тотемное животное - *Рысь*. Она олицетворяет такие качества, как скрытность, ловкость и острота зрения. \
Рыси известны своей способностью охотиться в условиях низкой освещенности и быстротой реакции. \
Если ваше тотемное животное рысь, то возможно вы обладаете этими качествами и способны быстро адаптироваться к \
изменяющимся обстоятельствам. Также, возможно, вы цените независимость и предпочитаете решать проблемы самостоятельно, \
как и рыси, которые обычно ведут одиночный образ жизни.', 'lynx.jpg'],
    '1930': ['🦄 Ваше тотемное животное - *Осёл*. Он олицетворяет такие качества, как трудолюбие, упорство и практичность. \
Ослы известны своей способностью работать долгие часы и перевозить тяжелые грузы. Если ваше тотемное животное осёл, \
то возможно вы обладаете этими качествами и способны усердно работать для достижения своих целей. \
Также, возможно, вы цените практичность и умеете находить практические решения в сложных ситуациях, как и ослы, \
которые известны своей выносливостью и приспособляемостью к различным условиям.', 'donkey.jpg'],
    '1931': ['🐻‍❄️ Ваше тотемное животное - *Белый медведь*. Он олицетворяет такие качества, как сила, мощь и независимость. \
Белые медведи известны своей физической силой, способностью выживать в суровых условиях Арктики и вести одиночный образ жизни. \
Если ваше тотемное животное белый медведь, то возможно вы обладаете этими качествами и способны преодолевать \
трудности и достигать поставленных целей. Также, возможно, вы цените независимость и предпочитаете решать проблемы \
самостоятельно, как и белые медведи, которые обычно ведут одиночный образ жизни.', 'polarbear.jpg'],
    '1932': ['🦅 Ваше тотемное животное - *Орёл*. Он олицетворяет такие качества, как зоркость, величие и духовность. \
Орлы известны своей способностью видеть мельчайшие детали на большом расстоянии и вести величественный образ жизни. \
Если ваше тотемное животное орел, то возможно вы обладаете этими качествами и стремитесь к духовному развитию и \
совершенствованию. Также, возможно, вы цените свободу и независимость, как и орлы, которые способны летать на большие \
высоты и преодолевать огромные расстояния.', 'eagle.jpg'],
    '1933': ['🦊 Ваше тотемное животное - *Лисица*. Она олицетворяет такие качества, как хитрость, ловкость и приспособляемость. \
Лисы известны своей способностью обманывать своих врагов и приспосабливаться к различным условиям среды. \
Если ваше тотемное животное лисица, то возможно вы обладаете этими качествами и способны находить нестандартные \
решения в сложных ситуациях. Также, возможно, вы цените свободу и независимость, как и лисы, которые предпочитают жить в \
одиночку или небольшими группами.', 'fox.jpg'],
    '1934': ['🐬 Ваше тотемное животное - *Дельфин*. Он олицетворяет такие качества, как игривость, интуиция и коммуникабельность. \
Дельфины известны своей дружелюбностью, игривым характером и способностью общаться друг с другом и с людьми. \
Если ваше тотемное животное дельфин, то возможно вы обладаете этими качествами и способны легко находить общий язык \
с людьми и животными. Также, возможно, вы цените радость и игривость в жизни и умеете наслаждаться каждым моментом, \
как и дельфины, которые известны своей игривой натурой.', 'delfin.jpg'],
    '1935': ['🐗 Ваше тотемное животное - *Вепрь*. Он олицетворяет такие качества, как сила, свирепость и бесстрашие. \
Вепри известны своей физической мощью, способностью защищать свою территорию и смелостью в атаке. \
Если ваше тотемное животное вепрь, то возможно вы обладаете этими качествами и способны смело стоять на защите \
своих интересов и ценностей. Также, возможно, вы цените силу и авторитет, как и вепри, которые являются символом \
власти и могущества в некоторых культурах.', 'boar.jpg'],
    '1936': ['🦉 Ваше тотемное животное - *Филин*. Он олицетворяет такие качества, как мудрость, интуиция и ночная активность. \
Филины известны своей способностью видеть в темноте и охотиться ночью. Если ваше тотемное животное филин, \
то возможно вы обладаете этими качествами и способны видеть вещи, которые другие не замечают. Также, возможно, \
вы цените мудрость и интуицию, как и филины, которые считаются символами мудрости и пророчества в некоторых культурах.', 'owl.jpg'],
    '1937': ['🦅 Ваше тотемное животное - *Сокол*. Он олицетворяет такие качества, как быстрота, острота зрения и способность \
достигать цели. Соколы известны своей невероятной скоростью и точностью в охоте. Если ваше тотемное животное сокол, \
то возможно вы обладаете этими качествами и стремитесь к достижению своих целей с максимальной эффективностью. \
Также, возможно, вы цените свободу и независимость, как и соколы, которые предпочитают жить в одиночку или небольшими группами.', 'falcon.jpg']
}
