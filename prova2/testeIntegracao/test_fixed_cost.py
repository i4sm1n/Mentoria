from utils.main_funtions import *

class TestFixedCost(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_fixed_cost(self):
        id_company = get_id(self.header)
        params = {'companyId': id_company}

        response = requests.get(f"{URL}/fixed-cost/{id_company}", params=params, headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        edition = json_data['edition']
        assert_in("socialCharges_company", edition)
        assert_equal(type(edition['socialCharges_company']), float)

        assert_in("min_salary", edition)
        assert_equal(type(edition['min_salary']), float)

        assert_in("max_salary", edition)
        assert_equal(type(edition['max_salary']), float)

        fixedCost = json_data['fixedCost']
        assert_in("for_rent", fixedCost)
        assert_equal(type(fixedCost['for_rent']), float)

        assert_in("office_supplies", fixedCost)
        assert_equal(type(fixedCost['office_supplies']), float)

        salary = json_data['salarys']
        i = 0
        for salary[i] in json_data['salarys']:
            assert_in("id", salary[i])
            assert_equal(type(salary[i]['id']), int)

            assert_in("role", salary[i])

            role = salary[i]['role']
            assert_in("id", role)
            assert_equal(type(role['id']), int)

            assert_in("name", role)
            assert_equal(type(role['name']), str)

            assert_in("value", salary[i])
            assert_equal(type(salary[i]['value']), float)

            i += 1
            if i == 3:
                break

        formula = json_data['formulas']
        assert_in("sumOfRentFixedCosts", formula)
        assert_equal(type(formula['sumOfRentFixedCosts']), float)

        assert_in("sumSalaryFixedCosts", formula)
        assert_equal(type(formula['sumSalaryFixedCosts']), float)

        assert_in("sumOfSocialChargesFixedCosts", formula)
        assert_equal(type(formula['sumOfSocialChargesFixedCosts']), float)

        assert_in("otherFixedCosts", formula)
        assert_equal(type(formula['otherFixedCosts']), float)

        assert_in("paySalary", json_data)
        assert_equal(type(json_data['paySalary']), bool)

        assert_in("hasActionsPermission", json_data)
        assert_equal(type(json_data['hasActionsPermission']), bool)