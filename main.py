
from job_manager.abc import HeadHunterAPI, SuperJobAPI
from job_manager.jsonsave import JSONSaver


def user_interaction():
    vacancies_json = []
    search_query = input( "Введите название вакансии  ")

    hh = HeadHunterAPI(search_query)
    sj = SuperJobAPI(search_query)
    for api in (hh, sj):
        api.get_vacancies(pages_count=8)
        vacancies_json.extend(api.modify_data())

    connector = JSONSaver(search_query=search_query, vacancies_json=vacancies_json)
    connector.select()

    while True:
        command = input(
                        "1 - Вывести весь список вакансий;\n"
                        "2 - Вывести вакансии не требующие опыт работы;\n"
                        "3 - Отсортировать по минимальной зарплате;\n"
                        "4 - Отсортировать по максимальной зарплате;\n" 
                        "5 - Вывести вакансии только крупных компаний;\n"
                        "выход - для записи списка вакансий и выхода;\n"

                        )
        if command.lower() == 'выход':
            break
        elif command == "1":
            vacancies = connector.select()
        elif command == "2":
            vacancies = connector.select_to()
        elif command == "3":
            vacancies = connector.sort_by_salary_from()
        elif command == "4":
            vacancies = connector.sort_by_salary_to()
        elif command == "5":
            vacancies = connector.select_tow()

        for vacanc in vacancies:
            print(vacanc, end='\n')


if __name__ == "__main__":
    user_interaction()
