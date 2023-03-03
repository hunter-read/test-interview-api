import json
import requests
from database import Database


def main():
    domain: str = "https://startplaying.games/api/detect-magic/gms?page="
    page = 0
    count = 0
    with Database() as db:
        while True:
            data = requests.get(f'{domain}{page}')
            results = json.loads(data.text)
            if len(results["gms"]) == 0:
                break;
            for gm in results["gms"]:
                count += 1
                gm_profile = gm['gmProfile']
                gm_stats = gm_profile['gmStats']
                params = [gm['id'], gm['created'], gm['image'], gm['lastname'],
                            gm['modified'], gm['name'], gm['pronouns'], gm['username'], 0, 
                            gm_profile['description'], gm_profile['yearsOfProfessionalGmExperience'],
                            gm_profile['yearsOfTtrpgExperience'], gm_stats['nextSessionStartTime'],
                            gm_stats['numReviews']]
                db.save(
                f"""
                    INSERT INTO gms (id, created, image, lastname, modified, name, pronouns, 
                        username, lookup_count, description, years_of_professional_gm_experience,
                        years_of_ttrpg_experience, next_session_start_time, number_reviews) VALUES (
                            ?, ?, ?, ?, ?, ?, ?,
                            ?, ?, ?, ?, ?, ?, ?);
                 """, params)
            page += 1
            print(count)


if __name__ == "__main__":
    main()
