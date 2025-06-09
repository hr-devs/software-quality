import sqlite3
from database.database_connection import DatabaseConnection
from encryptor import Encryptor
from database.repositories.activity_log_repository import ActivityLogRepository
from database.repositories.role_repository import RoleRepository
from database.repositories.scooter_repository import ScooterRepository
from database.repositories.traveller_repository import TravellerRepository
from database.repositories.user_repository import UserRepository

class DatabaseManager:
    def __init__(self, db_connection: DatabaseConnection = None):
        self.db_connection = db_connection
        
        # Initialize repos so we can use them in this class
        self.user_repo = UserRepository(self.db_connection)
        self.role_repo = RoleRepository(self.db_connection)
        self.traveller_repo = TravellerRepository(self.db_connection)
        self.scooter_repo = ScooterRepository(self.db_connection)
        self.activity_log_repo = ActivityLogRepository(self.db_connection)
    
    def initialize_database(self):
        # Using the repos to create all tables instead of 1 big query
        # ERror if something goes wrong
        try:
            self.user_repo.create_table()
            self.role_repo.create_table()
            self.traveller_repo.create_table()
            self.scooter_repo.create_table()
            self.activity_log_repo.create_table()
            
            self.populate_dummy_data()
            print("Database initialized successfully!")
            
        except Exception as e:
            print(f"Error initializing database: {e}")
            raise

    def populate_dummy_data(self):
        try:
            # Clear data
            self.user_repo.clear_all()
            self.role_repo.clear_all()
            self.traveller_repo.clear_all()
            self.scooter_repo.clear_all()
            self.activity_log_repo.clear_all()
            
            # Populate roles
            roles_data = [
                (1, 'super_admin'),
                (2, 'system_admin'),
                (3, 'service_engineer'),
            ]
            
            self.role_repo.insert_roles(roles_data)
            
            # Insert users
            users_data = [
                (Encryptor.encrypt_data('sup_adm01'), Encryptor.hash_pwd('SuperAdmin#2024!'), 1),
                (Encryptor.encrypt_data('sys_adm02'), Encryptor.hash_pwd('SysControl&Pass9'), 2),
                (Encryptor.encrypt_data('svc_eng03'), Encryptor.hash_pwd('Engineer@Service7'), 3)
            ]
            
            self.user_repo.insert_users( users_data)
            
            # Insert travellers
            travellers_data = [
                ('Jan', 'de Vries', '1985-03-15', 'male', 'Coolsingel', 42, '3012 AA', 'Rotterdam', 'jan.devries@email.nl', '+31-6-12345678', 'NL123456789'),
                ('Sarah', 'van der Berg', '1992-07-22', 'female', 'Witte de Withstraat', 15, '3012 BK', 'Rotterdam', 'sarah.vandenberg@email.nl', '+31-6-23456789', 'NL234567890'),
                ('Mike', 'Thompson', '1988-11-08', 'male', 'Erasmusbrug', 3, '3011 BN', 'Rotterdam', 'mike.thompson@email.com', '+31-6-34567890', '123456789NL')
            ]
            
            self.traveller_repo.insert_travellers( travellers_data)
            
            # Populate scooters
            scooters_data = [
                ('Segway', 'Ninebot MAX G30', 'SG2024001ABC', 25, 551, 85.5, 20.0, 90.0, 'Excellent condition', 51.92250, 4.47917, 0, 1245.8, '2024-01-15'),
                ('NIU', 'KQi3 Pro', 'NIU2024002DEF', 25, 486, 67.2, 15.0, 85.0, 'Recently serviced', 51.91845, 4.48234, 0, 892.3, '2024-02-10'),
                ('Xiaomi', 'Mi Electric Scooter 3', 'XM2024003GHI', 25, 275, 45.8, 10.0, 80.0, 'Good working order', 51.92456, 4.47652, 0, 654.1, '2024-01-28')
            ]
            
            self.scooter_repo.insert_scooters(scooters_data)
            
            # Insert activity logs
            activity_logs_data = [
                ('2024-06-04', '08:15:32', 'superadmin', 'Logged in', 'System startup'),
                ('2024-06-04', '08:16:45', 'superadmin', 'Database backup created', 'Scheduled backup'),
                ('2024-06-04', '09:23:12', 'admin_rotterdam', 'Logged in', 'Morning shift start')
            ]
            
            self.activity_log_repo.insert_activity_logs(activity_logs_data)

        except Exception as e:
            print(f"Error populating dummy data: {e}")
            raise

        try:
            print("Sample travellers data:", self.user_repo.fetch_all())
        except Exception as e:
            print("Error fetching data")
            raise
