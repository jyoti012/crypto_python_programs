from datetime import datetime


def calculate_bill_share_diff_dates(year, month, bill_name, bill_cost,
                                    sharing_details):
  # Correcting the calculation for days_in_month
  days_in_month = (
      datetime(year if month < 12 else year + 1, month % 12 + 1, 1) -
      datetime(year, month, 1)).days
  total_bill_per_day = bill_cost / days_in_month
  roommate_shares = {}

  for detail in sharing_details:
    roommates = detail['roommates']
    start_date = datetime(year, month, detail['start_date'])
    end_date = datetime(year, month, detail['end_date'])
    days_shared = (end_date - start_date).days + 1
    cost_for_period = total_bill_per_day * days_shared

    for roommate in roommates:
      if roommate not in roommate_shares:
        roommate_shares[roommate] = 0
      roommate_shares[roommate] += cost_for_period / len(roommates)

  results = f'Bill: {bill_name} for Month: {month}/{year}\n'
  for roommate, share in roommate_shares.items():
    results += f"{roommate}'s share: ${share:.2f}\n"
  print(results)
# # Example usage
calculate_bill_share_diff_dates(2023, 8, 'Wifi', 45,
                                [{
                                    'roommates': ['Sayli'],
                                    'start_date': 1,
                                    'end_date': 5
                                }, {
                                    'roommates': ['Sayli', 'Jyoti'],
                                    'start_date': 6,
                                    'end_date': 28
                                }, {
                                    'roommates': ['Jenny', 'Sayli', 'Jyoti'],
                                    'start_date': 29,
                                    'end_date': 31
                                }])

calculate_bill_share_diff_dates(2023, 9, 'Wifi', 45,
                                [{
                                    'roommates': ['Jenny', 'Sayli', 'Jyoti'],
                                    'start_date': 1,
                                    'end_date': 11
                                }, {
                                    'roommates': ['Anshal', 'Jenny', 'Jyoti'],
                                    'start_date': 12,
                                    'end_date': 30
                                }])

calculate_bill_share_diff_dates(2023, 10, 'Wifi', 45,
                                [{
                                    'roommates': ['Jenny', 'Anshal', 'Jyoti'],
                                    'start_date': 1,
                                    'end_date': 15
                                }, {
                                    'roommates': ['Anshal', 'Jenny', 'Jyoti', 'Sayli'],
                                    'start_date': 16,
                                    'end_date': 31
                                }])

calculate_bill_share_diff_dates(
    2023, 11, 'Wifi', 45, [{
        'roommates': ['Anshal', 'Jenny', 'Jyoti', 'Sayli'],
        'start_date': 1,
        'end_date': 30
    }])

calculate_bill_share_diff_dates(
    2023, 12, 'Wifi', 45, [{
        'roommates': ['Anshal', 'Jenny', 'Jyoti', 'Sayli'],
        'start_date': 1,
        'end_date': 31
    }])

calculate_bill_share_diff_dates(
    2024, 1, 'Wifi', 45, [{
        'roommates': ['Anshal', 'Jenny', 'Jyoti', 'Sayli'],
        'start_date': 1,
        'end_date': 17
    }, {
        'roommates': ['Jenny', 'Anshal', 'Jyoti'],
        'start_date': 18,
        'end_date': 31
    }])
