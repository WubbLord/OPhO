from utils import run_async, get_connection

problem_number = 35
#run after creating user_details_2023
async def execute():
    conn = await get_connection()
    team_ids = []
    for i in range(1,978):
        team_ids.append(i)
    
    for team_id in team_ids:
        create_table = f"""
        CREATE TABLE team{team_id}(problem_no integer references problems,solved BOOLEAN NOT NULL, attempts integer, answers decimal[], timestamp timestamp);
        """
        insert_query = f"""
            INSERT INTO team{team_id} (problem_no, solved, attempts) VALUES """ + ', '.join(f"({number}, FALSE, 0)" for number in range(1, problem_number+1)) + ";"
        
        await conn.execute(create_table)
        await conn.execute(insert_query)

        print("CREATING TEAM TABLE", team_id)

run_async(execute())

    