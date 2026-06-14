from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Job Roles Database
job_roles = {
    "Data Scientist":
        "python machine_learning sql data_analysis statistics pandas numpy tensorflow deep_learning",

    "ML Engineer":
        "python tensorflow pytorch machine_learning deep_learning model_deployment docker kubernetes",

    "Backend Developer":
        "python java nodejs sql rest_api databases django flask microservices",

    "Frontend Developer":
        "javascript react html css nodejs typescript web_design ui_ux",

    "DevOps Engineer":
        "docker kubernetes aws linux ci_cd automation git jenkins cloud",

    "Cloud Architect":
        "aws azure cloud docker kubernetes networking security infrastructure terraform",

    "Data Analyst":
        "sql excel python data_analysis statistics visualization power_bi tableau reporting",

    "AI Researcher":
        "python machine_learning deep_learning tensorflow research mathematics statistics nlp",

    "Cybersecurity Engineer":
        "networking security linux ethical_hacking encryption firewalls python penetration_testing",

    "Full Stack Developer":
        "javascript react nodejs python sql html css rest_api databases git",

    "Mobile Developer":
        "flutter dart java kotlin swift ios android react_native mobile_ui",

    "Database Administrator":
        "sql mysql postgresql mongodb database_design optimization backup indexing oracle"
}

role_names = list(job_roles.keys())
role_skills = list(job_roles.values())

vectorizer = TfidfVectorizer()
role_matrix = vectorizer.fit_transform(role_skills)

print("=" * 60)
print("   PROJECT 3: AI TECH STACK RECOMMENDER")
print("   Powered by TF-IDF + Cosine Similarity")
print("=" * 60)
print(f"\n📚 Knowledge Base loaded: {len(role_names)} job roles")
print(f"🔤 Vocabulary size: {len(vectorizer.vocabulary_)} unique skills")


def get_recommendations(user_skills_list, top_n=3):
    user_input_string = " ".join(user_skills_list).lower()
    user_vector = vectorizer.transform([user_input_string])

    similarity_scores = cosine_similarity(user_vector, role_matrix)[0]

    sorted_indices = np.argsort(similarity_scores)[::-1]
    top_indices = sorted_indices[:top_n]

    results = []

    for idx in top_indices:
        role = role_names[idx]
        score = similarity_scores[idx]

        if score > 0:
            results.append((role, score))

    return results


print("\n" + "=" * 60)
print("              SKILL INPUT PHASE")
print("=" * 60)

print("\nAvailable skill examples:")
print("python, java, javascript, sql, machine_learning,")
print("deep_learning, tensorflow, docker, kubernetes, aws,")
print("react, nodejs, html, css, data_analysis, statistics,")
print("networking, security, flutter, excel, git, linux\n")

user_skills = []

print("Enter your skills one by one (minimum 3).")
print("Type 'done' when finished.\n")

while True:
    skill = input(f"Skill {len(user_skills)+1}: ").strip().lower()

    if skill == "done":
        if len(user_skills) < 3:
            print(f"❌ Please enter at least 3 skills! You have {len(user_skills)} so far.")
        else:
            break

    elif skill == "":
        print("⚠️ Please enter a skill or type 'done'")

    else:
        skill = skill.replace(" ", "_")
        user_skills.append(skill)
        print(f"✅ Added: {skill}")

print("\n" + "=" * 60)
print("           RUNNING SIMILARITY ENGINE...")
print("=" * 60)

print(f"\n🧑 Your Skills Profile: {user_skills}")
print(f"🔍 Comparing against {len(role_names)} job roles...")

recommendations = get_recommendations(user_skills, top_n=3)

print("\n" + "=" * 60)
print("         🏆 YOUR TOP CAREER RECOMMENDATIONS")
print("=" * 60)

if not recommendations:
    print("\n❌ No matches found! Try using skill names from the list above.")
else:
    for rank, (role, score) in enumerate(recommendations, start=1):
        percentage = score * 100
        bar_length = int(percentage / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)

        print(f"\n#{rank} {role}")
        print(f"Match Score : {percentage:.1f}%")
        print(f"[{bar}]")

print("\n" + "=" * 60)
print("         📊 SKILL MATCH BREAKDOWN")
print("=" * 60)

for role, score in recommendations:
    role_idx = role_names.index(role)
    role_skill_list = role_skills[role_idx].split()

    matched = [s for s in user_skills if s in role_skill_list]
    missing = [s for s in role_skill_list if s not in user_skills][:3]

    print(f"\n{role} ({score*100:.1f}% match)")
    print(f"✅ Skills you have : {matched if matched else 'indirect match'}")
    print(f"📌 Skills to learn : {missing}")

print("\n" + "=" * 60)
print("Keep building your skills! Every expert was once a beginner.")
print("=" * 60)