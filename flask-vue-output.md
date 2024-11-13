# Project Documentation
Generated on: 2024-11-13 13:02:06

## Table of Contents


### home/milav/code/gppLMSv2/backend/app/apis
- [crud.py](#crud-py)
- [__init__.py](#__init__-py)
- [main.py](#main-py)

### home/milav/code/gppLMSv2/backend/app
- [extensions.py](#extensions-py)
- [forms.py](#forms-py)
- [__init__.py](#__init__-py)
- [models.py](#models-py)

### home/milav/code/gppLMSv2/backend/app/routes
- [auth.py](#auth-py)
- [crud_api_calls.py](#crud_api_calls-py)
- [__init__.py](#__init__-py)
- [librarian.py](#librarian-py)
- [main.py](#main-py)
- [member.py](#member-py)

### home/milav/code/gppLMSv2/backend/app
- [schemas.py](#schemas-py)
- [services.py](#services-py)

### home/milav/code/gppLMSv2/backend/app/templates/admin
- [index.html](#index-html)

### home/milav/code/gppLMSv2/backend/app/templates
- [base.html](#base-html)
- [index.html](#index-html)

### home/milav/code/gppLMSv2/backend/app/templates/librarian
- [edit.html](#edit-html)
- [home.html](#home-html)
- [list.html](#list-html)
- [user_add.html](#user_add-html)
- [user_delete.html](#user_delete-html)
- [user_edit.html](#user_edit-html)
- [user_list.html](#user_list-html)
- [user_view.html](#user_view-html)

### home/milav/code/gppLMSv2/backend/app/templates/main
- [select_role.html](#select_role-html)

### home/milav/code/gppLMSv2/backend/app/templates/member
- [books.html](#books-html)
- [browse_books.html](#browse_books-html)
- [browse_genres.html](#browse_genres-html)
- [home.html](#home-html)
- [loans.html](#loans-html)

### home/milav/code/gppLMSv2/backend/app/templates/security
- [base.html](#base-html)
- [change_password.html](#change_password-html)

### home/milav/code/gppLMSv2/backend/app/templates/security/email
- [confirmation_instructions.html](#confirmation_instructions-html)
- [reset_instructions.html](#reset_instructions-html)
- [reset_notice.html](#reset_notice-html)
- [welcome.html](#welcome-html)

### home/milav/code/gppLMSv2/backend/app/templates/security
- [forgot_password.html](#forgot_password-html)
- [login_user.html](#login_user-html)
- [register_user.html](#register_user-html)
- [reset_password.html](#reset_password-html)

### home/milav/code/gppLMSv2/backend/app
- [views.py](#views-py)

### home/milav/code/gppLMSv2/backend
- [config.py](#config-py)
- [db_migrator.sh](#db_migrator-sh)
- [local_gunicorn.sh](#local_gunicorn-sh)
- [local_mailhog.sh](#local_mailhog-sh)
- [local_run.sh](#local_run-sh)
- [local_setup.sh](#local_setup-sh)
- [local_testing.sh](#local_testing-sh)
- [main.py](#main-py)

### home/milav/code/gppLMSv2/frontend
- [babel.config.js](#babel-config-js)

### home/milav/code/gppLMSv2/frontend/public
- [index.html](#index-html)

### home/milav/code/gppLMSv2/frontend/src
- [App.vue](#app-vue)
- [axiosConfig.js](#axiosconfig-js)

### home/milav/code/gppLMSv2/frontend/src/components/auth
- [ChangePassword.vue](#changepassword-vue)
- [ForgotPassword.vue](#forgotpassword-vue)
- [ProfileComponent.vue](#profilecomponent-vue)
- [UserLogin.vue](#userlogin-vue)
- [UserLogout.vue](#userlogout-vue)
- [UserRegistration.vue](#userregistration-vue)

### home/milav/code/gppLMSv2/frontend/src/components/BookBrowsing
- [BrowseBooks.vue](#browsebooks-vue)
- [BrowseGenre.vue](#browsegenre-vue)
- [CardComponent.vue](#cardcomponent-vue)
- [FilterSection.vue](#filtersection-vue)
- [SideMenu.vue](#sidemenu-vue)

### home/milav/code/gppLMSv2/frontend/src/components
- [BookLoanDetailsComponent.vue](#bookloandetailscomponent-vue)
- [BookLoanRequestComponent.vue](#bookloanrequestcomponent-vue)
- [BookLoanRequestsListComponent.vue](#bookloanrequestslistcomponent-vue)
- [BookLoansListComponent.vue](#bookloanslistcomponent-vue)
- [BrowseBooks.vue](#browsebooks-vue)
- [BrowseGenres.vue](#browsegenres-vue)
- [BrowseGenre.vue](#browsegenre-vue)
- [FilterSection.vue](#filtersection-vue)
- [GeneralEdit.vue](#generaledit-vue)
- [GeneralList.vue](#generallist-vue)
- [RoleSelectionComponent.vue](#roleselectioncomponent-vue)
- [SearchBar.vue](#searchbar-vue)
- [SideMenu.vue](#sidemenu-vue)
- [UserProfileEditComponent.vue](#userprofileeditcomponent-vue)
- [UserProfileViewComponent.vue](#userprofileviewcomponent-vue)

### home/milav/code/gppLMSv2/frontend/src
- [config.js](#config-js)
- [main.js](#main-js)

### home/milav/code/gppLMSv2/frontend/src/router
- [index.js](#index-js)

### home/milav/code/gppLMSv2/frontend/src/services
- [ApiService.js](#apiservice-js)

### home/milav/code/gppLMSv2/frontend/src
- [store.js](#store-js)

### home/milav/code/gppLMSv2/frontend/src/utils
- [filterBooks.js](#filterbooks-js)

### home/milav/code/gppLMSv2/frontend/src/views
- [AboutView.vue](#aboutview-vue)
- [BrowseLibraryView.vue](#browselibraryview-vue)
- [HomeView.vue](#homeview-vue)
- [LibrarianDashboardView.vue](#librariandashboardview-vue)
- [MemberDashboardView.vue](#memberdashboardview-vue)
- [MyLoansView.vue](#myloansview-vue)
- [ProfileView.vue](#profileview-vue)

### home/milav/code/gppLMSv2/frontend
- [vue.config.js](#vue-config-js)

---

## crud.py
Path: `/home/milav/code/gppLMSv2/backend/app/apis/crud.py`

```py
from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import desc, or_
from urllib.parse import parse_qs
from app.models import (
    db,
    user_datastore,
    User,
    Book,
    Genre,
    Author,
    Member,
    Librarian,
    BookLoan
)
from app.schemas import (
    BookSchema,
    GenreSchema,
    AuthorSchema,
    UserSchema,
    MemberSchema,
    LibrarianSchema,
    BookLoanSchema
)
# from flask_security import login_required

crud_api_bp = Blueprint("crud_api_bp", __name__)
crud_api = Api(crud_api_bp)


class BaseApi(Resource):
    model = None
    schema = None

    def get(self, id=None):
        if id:
            obj = self.model.query.get_or_404(id)
            return self.schema.dump(obj)
        else:
            query = self.model.query
            query = self.apply_filters(query)
            query = self.apply_sorting(query)
            objs = query.all()
            return self.schema.dump(objs, many=True)

    def apply_filters(self, query):
        for key in request.args:
            if key.startswith('filters['):
                # Extracting the actual filter key from 'filters[<key>]'
                filter_key = key[8:-1]  # Removes 'filters[' and ']'
                if hasattr(self.model, filter_key):
                    filter_value = request.args[key]
                    query = query.filter(getattr(self.model, filter_key) == filter_value)
        return query

        for key in request.args:
            if key.startswith('filters['):
                filter_key = key[8:-1]  # Removes 'filters[' and ']'
                filter_value = request.args[key]
                
                if '__' in filter_key:
                    # Handle relationships (e.g., 'genres__name')
                    relationship, field = filter_key.split('__')
                    if hasattr(self.model, relationship):
                        related_model = getattr(self.model, relationship).property.mapper.class_
                        if hasattr(related_model, field):
                            query = query.join(related_model).filter(getattr(related_model, field) == filter_value)
                elif filter_key.endswith('__in'):
                    # Handle 'in' conditions (e.g., 'id__in')
                    actual_key = filter_key[:-4]
                    if hasattr(self.model, actual_key):
                        filter_values = filter_value.split(',')
                        query = query.filter(getattr(self.model, actual_key).in_(filter_values))
                elif filter_key.endswith('__contains'):
                    # Handle 'contains' conditions (e.g., 'title__contains')
                    actual_key = filter_key[:-10]
                    if hasattr(self.model, actual_key):
                        query = query.filter(getattr(self.model, actual_key).contains(filter_value))
                else:
                    # Handle simple equality conditions
                    if hasattr(self.model, filter_key):
                        query = query.filter(getattr(self.model, filter_key) == filter_value)
        
        return query    


        for key in request.args:
            if key.startswith('filters['):
                filter_key = key[8:-1]  # Removes 'filters[' and ']'
                filter_value = request.args[key]
                
                if '__' in filter_key:
                    # Handle relationships (e.g., 'genres__name')
                    relationship, field = filter_key.split('__')
                    if hasattr(self.model, relationship):
                        related_model = getattr(self.model, relationship).mapper.class_
                        if hasattr(related_model, field):
                            query = query.join(related_model).filter(getattr(related_model, field) == filter_value)
                elif filter_key.endswith('__in'):
                    # Handle 'in' conditions (e.g., 'id__in')
                    actual_key = filter_key[:-4]
                    if hasattr(self.model, actual_key):
                        filter_values = filter_value.split(',')
                        query = query.filter(getattr(self.model, actual_key).in_(filter_values))
                elif filter_key.endswith('__contains'):
                    # Handle 'contains' conditions (e.g., 'title__contains')
                    actual_key = filter_key[:-10]
                    if hasattr(self.model, actual_key):
                        query = query.filter(getattr(self.model, actual_key).contains(filter_value))
                else:
                    # Handle simple equality conditions
                    if hasattr(self.model, filter_key):
                        query = query.filter(getattr(self.model, filter_key) == filter_value)
        
        return query
    def apply_sorting(self, query):
        sort_by = request.args.get('sort_by')
        sort_order = request.args.get('sort_order', 'asc')

        if sort_by and hasattr(self.model, sort_by):
            sort_column = getattr(self.model, sort_by)
            if sort_order == 'desc':
                query = query.order_by(desc(sort_column))
            else:
                query = query.order_by(sort_column)
        return query

    def post(self):
        obj = self.schema.load(request.json)
        db.session.add(obj)
        db.session.commit()
        return self.schema.dump(obj), 201

    def put(self, id):
        obj = self.model.query.get_or_404(id)
        updated_obj = self.schema.load(request.json, instance=obj)
        db.session.commit()
        return self.schema.dump(updated_obj)

    def delete(self, id):
        obj = self.model.query.get_or_404(id)
        db.session.delete(obj)
        db.session.commit()
        return "", 204


class UserApi(BaseApi):
    model = User
    schema = UserSchema()

    def post(self):
        schema = UserSchema(load_instance=False)
        data = schema.load(request.json)
        user = user_datastore.create_user(**data)
        db.session.add(user)
        db.session.commit()
        return self.schema.dump(user), 201


class MemberApi(UserApi):
    model = Member
    schema = MemberSchema()


class LibrarianApi(UserApi):
    model = Librarian
    schema = LibrarianSchema()


class BookApi(BaseApi):
    model = Book
    schema = BookSchema()


class GenreApi(BaseApi):
    model = Genre
    schema = GenreSchema()


class AuthorApi(BaseApi):
    model = Author
    schema = AuthorSchema()

class BookLoanApi(BaseApi):
    model = BookLoan
    schema = BookLoanSchema()    


def add_resource_routes(api, resource_api_class, endpoint_name, id_type="int"):
    api.add_resource(
        resource_api_class, f"/api/{endpoint_name}", endpoint=f"{endpoint_name}_list"
    )
    api.add_resource(
        resource_api_class,
        f"/api/{endpoint_name}/<{id_type}:id>",
        endpoint=f"{endpoint_name}",
    )


# Add routes for BookApi, GenreApi, AuthorApi, etc.
add_resource_routes(crud_api, BookApi, "books")
add_resource_routes(crud_api, GenreApi, "genres")
add_resource_routes(crud_api, AuthorApi, "authors")
add_resource_routes(crud_api, UserApi, "users")
add_resource_routes(crud_api, MemberApi, "members")
add_resource_routes(crud_api, LibrarianApi, "librarians")
add_resource_routes(crud_api, BookLoanApi, "bookloans")

```

## __init__.py
Path: `/home/milav/code/gppLMSv2/backend/app/apis/__init__.py`

```py


```

## main.py
Path: `/home/milav/code/gppLMSv2/backend/app/apis/main.py`

```py
from flask import Blueprint, jsonify, request, url_for
from flask_login import current_user
from flask_security import auth_required, login_required
from datetime import datetime
from ..models import db, BookLoan, User
from ..schemas import book_loan_schema, book_loans_schema, user_schema, profile_schema

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/api/select_role", methods=["GET", "POST"])
# @auth_required("token", "session")
@login_required
def select_role():
    data = request.json
    selected_role = data.get("role")
    if selected_role:
        if selected_role == "Librarian":
            return jsonify({"redirect_url": url_for("librarian_bp.home")})
        elif selected_role == "Member":
            return jsonify({"redirect_url": url_for("member_bp.home")})
    
    return jsonify({"error": "Invalid role selected"}), 400


# Get loans for a member
@api_bp.route("/api/bookloans/members/<int:member_id>", methods=['GET'])
def get_loans_by_member(member_id):
    loans = BookLoan.query.filter_by(member_id=member_id).all()
    return book_loans_schema.jsonify(loans)



# Get loans for a book
@api_bp.route("/api/bookloans/books/<int:book_id>", methods=['GET'])
def get_loans_by_book(book_id):
    loans = BookLoan.query.filter_by(book_id=book_id).all()
    return book_loans_schema.jsonify(loans)


# Approve loan
@api_bp.route("/api/bookloans/<int:loan_id>/approve", methods=["PUT"])
def approve_loan(loan_id):
    loan = BookLoan.query.get(loan_id)
    loan.status = "approved"
    db.session.commit()
    return book_loan_schema.jsonify(loan)


# Return loan
@api_bp.route("/api/bookloans/<int:loan_id>/return", methods=["PUT"])
def return_loan(loan_id):
    loan = BookLoan.query.get(loan_id)
    # loan.returned_date = datetime.utcnow().date()
    loan.returned_date = datetime.now(datetime.timezone.utc).date()
    loan.status = "returned"
    db.session.commit()
    return book_loan_schema.jsonify(loan)


@api_bp.route('/api/current_user', methods=['GET'])
@login_required
def get_current_user():
    return user_schema.jsonify(current_user)


@api_bp.route('/api/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    user = User.query.get(user_id)
    if user:
        return profile_schema.jsonify(user)
    return jsonify({"error": "User not found"}), 404

@api_bp.route('/api/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    user = User.query.get(user_id)
    if user:
        updated_profile = profile_schema.load(request.json, instance=user, partial=True)
        db.session.commit()
        return profile_schema.jsonify(updated_profile)
    return jsonify({"error": "User not found"}), 404

```

## extensions.py
Path: `/home/milav/code/gppLMSv2/backend/app/extensions.py`

```py
# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_security import Security
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_babel import Babel
from flask_cors import CORS
# from flask_babelex import Babel
# from flask_admin import Admin
# from flask_caching import Cache
# from flask_moment import Moment
# from flask_jwt_extended import JWTManager
# from flask_login import LoginManager

# from flask_principal import Principal
# from flask_session import Session
# from flask_oauthlib.client import OAuth
# from flask_uploads import UploadSet, IMAGES
# from flask_pydantic import validate



# Initialize extensions, but without any specific app bound to them.
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
mail = Mail()
security = Security()
ma = Marshmallow()
babel = Babel()
cors = CORS()
# login = LoginManager()
# cache = Cache()
# admin = Admin(name='Gpp', template_mode='bootstrap3')
# moment = Moment()
# jwt = JWTManager()

# principal = Principal()
# session = Session()
# oauth = OAuth()
# image_set = UploadSet("images", IMAGES)

```

## forms.py
Path: `/home/milav/code/gppLMSv2/backend/app/forms.py`

```py
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    SelectField,
    SelectMultipleField,
    DateField,
    TextAreaField,
    PasswordField,
)
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo
from .models import Role, Author, Book, Member, User, Genre, db
from flask_security import RegisterForm


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    isbn_13 = StringField("ISBN-13")
    isbn_10 = StringField("ISBN-10")
    publisher = StringField("Publisher")
    publication_date = DateField("Publication Date")  # Use StringField for simplicity
    language = StringField("Language")
    content = TextAreaField("Content")
    authors = QuerySelectMultipleField(
        "Authors", query_factory=lambda: Author.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")


class AuthorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    biography = StringField("Biography", validators=[DataRequired()])
    submit = SubmitField("Submit")


class GenreForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("User Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    type = SelectField("Type", coerce=str)
    roles = QuerySelectMultipleField(
        "Roles", query_factory=lambda: Role.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.type.choices = [
            (role.name.lower(), role.name) for role in Role.query.all()
        ]

class MemberForm(UserForm):
    preferred_genres = QuerySelectMultipleField(
        "Genre", query_factory=lambda: Genre.query.all(), get_label="name"
    )
    language_preference = StringField("Preferred Languages")
    # language_preference = SelectMultipleField(
    #     'Preferred Languages', 
    #     choices=[
    #         ('english', 'English'),
    #         ('hindi', 'Hindi'),
    #         ('gujarati', 'Gujarati'),
    #         ('others', 'Others')
    #     ],
    #     validators=[DataRequired()]
    # )

class RoleSelectForm(FlaskForm):
    roles = QuerySelectField(
        "Roles", query_factory=lambda: Role.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("User Name", validators=[DataRequired()])



class BookLoanForm(FlaskForm):
    book_id = QuerySelectField("Book", query_factory=lambda: Book.query.all(), get_label="title")
    member_id = QuerySelectField("Member", query_factory=lambda: Member.query.all(), get_label="email")
    # book_id = SelectField("Book", coerce=str) 
    # member_id = SelectField("Member", coerce=str)
    loan_date = DateField('Loan Date', validators=[DataRequired()])
    returned_date = DateField('Returned Date')
    status = SelectField(
        'Status', 
        choices=[
            ('requested', 'Requested'),
            ('approved', 'Approved'),
            ('active', 'Active'),
            ('overdue', 'Overdue'),
            ('returned', 'Returned')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit")

    # def __init__(self, *args, **kwargs):    
    #     super(BookLoanForm, self).__init__(*args, **kwargs)
    #     self.book_id.choices = [
    #         (book.id, book.title) for book in Book.query.all()
    #     ]
    #     self.member_id.choices = [
    #         (member.id, member.email) for member in Member.query.all()
    #     ]

```

## __init__.py
Path: `/home/milav/code/gppLMSv2/backend/app/__init__.py`

```py
from flask import Flask
from config import LocalDevelopmentConfig
from .extensions import db, migrate, security, bootstrap, mail, ma, babel, cors
from .apis.crud import crud_api_bp
from .apis.main import api_bp
from .routes.crud_api_calls import api_call_bp
from .routes.main import main_bp
from .routes.librarian import librarian_bp
from .routes.member import member_bp
from .routes.auth import auth_bp
from .utilities.utils import initialize_db
from .utilities.generate_dummy_data import generate_dummy_data
# import flask_excel as excel
# from flask_sse import sse
from .views import setup_admin
from .models import user_datastore
from .forms import ExtendedRegisterForm


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.app_context().push()
    

    mail.init_app(app)
    bootstrap.init_app(app)
    security.init_app(app, user_datastore, register_form=ExtendedRegisterForm)
    app.user_datastore = user_datastore

    # cache.init_app(app)
    # excel.init_excel(app)
    # admin.init_app(app)
    # moment.init_app(app)
    # login.init_app(app)
    babel.init_app(app)
    cors.init_app(app)
    setup_admin(app)
    with app.app_context():
        db.create_all()
        # generate_dummy_data()
        # initialize_db(user_datastore)
        # import app.views

    # Register Blueprints
    # app.register_blueprint(user_api_bp, user_datastore=user_datastore)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(crud_api_bp)
    app.register_blueprint(api_call_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(librarian_bp)
    # app.register_blueprint(main_bp)

    # # This is for streaming
    # app.register_blueprint(sse, url_prefix="/stream")
    # cors.init_app(app)

    return app

```

## models.py
Path: `/home/milav/code/gppLMSv2/backend/app/models.py`

```py
from app.extensions import db
from datetime import datetime, timedelta
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore


class CRUDMixin(db.Model):
    """
    Mixin that adds convenience methods for CRUD
    (create, read, update, delete) operations.
    """

    __abstract__ = True  # declares this as an abstract class

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()

    # Optional: Implement a method to serialize data, useful for APIs
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Association tables for many-to-many relationships
roles_users = db.Table(
    "roles_users",
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
)

member_books = db.Table(
    "member_books",
    db.Column("member_id", db.Integer(), db.ForeignKey("member.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)


membership_books = db.Table(
    "membership_books",
    db.Column("membership_id", db.Integer(), db.ForeignKey("membership.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

wishlist_books = db.Table(
    "wishlist_books",
    db.Column("wishlist_id", db.Integer(), db.ForeignKey("wishlist.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

collection_books = db.Table(
    "collection_books",
    db.Column("collection_id", db.Integer(), db.ForeignKey("collection.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

authors_books = db.Table(
    "authors_books",
    db.Column("author_id", db.Integer(), db.ForeignKey("author.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

genres_books = db.Table(
    "genres_books",
    db.Column("genre_id", db.Integer(), db.ForeignKey("genre.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)


class Role(RoleMixin, CRUDMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(UserMixin, CRUDMixin):
    __mapper_args__ = {"polymorphic_identity": "user", "polymorphic_on": "type"}
    id = db.Column(db.Integer, primary_key=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    roles = db.relationship(
        "Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic")
    )
    type = db.Column(db.String(50))


class Admin(User):
    __mapper_args__ = {"polymorphic_identity": "admin"}
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)


class Librarian(User):
    __mapper_args__ = {"polymorphic_identity": "librarian"}
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)


class Member(User):
    __mapper_args__ = {"polymorphic_identity": "member"}
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    membership_id = db.Column(db.Integer, db.ForeignKey("membership.id"))
    language_preference = db.Column(db.String(50))
    # Relationships
    reading_history = db.relationship(
        "Book", secondary=member_books, backref="member", lazy="dynamic"
    )
    book_loans = db.relationship("BookLoan", backref="member", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="member", lazy="dynamic")
    wishlists = db.relationship("Wishlist", backref="member", lazy="dynamic")
    collections = db.relationship("Collection", backref="member", lazy="dynamic")
    reviews = db.relationship("Review", backref="member", lazy="dynamic")
    preferred_genres = db.relationship("Genre", backref="member", lazy="dynamic")


class Membership(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # Silver, Gold, Platinum
    price = db.Column(db.Float)
    duration_type = db.Column(db.String(50))  # monthly, yearly, lifetime
    max_books_allowed = db.Column(db.Integer)
    discount_rate = db.Column(db.Float)  # Discount on purchases
    members = db.relationship("Member", backref="membership", lazy="dynamic")


class Wishlist(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Collection(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Genre(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Author(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String, nullable=False)


class Book(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)  # Use appropriate storage for book content
    isbn_13 = db.Column(db.String(13))  # ISBN-13
    isbn_10 = db.Column(db.String(10))  # ISBN-10
    publisher = db.Column(db.String(100))
    publication_date = db.Column(db.Date)
    language = db.Column(db.String(50))
    type = db.Column(db.String(50))  # Physical, eBook, Audiobook

    # Relationships: Many to Many
    authors = db.relationship(
        "Author", secondary=authors_books, backref="books", lazy="dynamic"
    )
    genres = db.relationship(
        "Genre", secondary=genres_books, backref="books", lazy="dynamic"
    )
    collections = db.relationship(
        "Collection", secondary=collection_books, backref="books", lazy="dynamic"
    )
    wishlists = db.relationship(
        "Wishlist", secondary=wishlist_books, backref="book", lazy="dynamic"
    )
    free_access_in_memberships = db.relationship(
        "Membership", secondary=membership_books, backref="book", lazy="dynamic"
    )
    # Relationships: One to Many
    book_loans = db.relationship("BookLoan", backref="book", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="book", lazy="dynamic")
    reviews = db.relationship("Review", backref="book", lazy="dynamic")


class BookLoan(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    loan_date = db.Column(db.Date, default=datetime.utcnow().date())
    due_date = db.Column(
        db.Date, default=lambda: datetime.utcnow().date() + timedelta(days=14)
    )
    returned_date = db.Column(db.Date)
    status = db.Column(
        db.String(20), default="issued"
    )  # Statuses like requested, issued, overdue, returned


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    price = db.Column(db.Float)
    price_after_discount = db.Column(db.Float)


class Review(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)  # e.g., 1-5
    review = db.Column(db.Text)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)

```

## auth.py
Path: `/home/milav/code/gppLMSv2/backend/app/routes/auth.py`

```py
from flask import Blueprint, render_template, redirect, url_for
# from app.forms import RegistrationForm, ExtendedRegisterForm
from app.models import user_datastore, db

auth_bp = Blueprint("auth_bp", __name__)


# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = ExtendedRegisterForm()

#     if form.validate_on_submit():
#         # Create a new user with the form data
#         user_datastore.create_user(
#             email=form.email.data,
#             password=form.password.data,
#             first_name=form.first_name.data,
#             last_name=form.last_name.data
#             # Set other user attributes
#         )
#         db.session.commit()

#         # Redirect to the login page or any other page as needed
#         return redirect(url_for('security.login'))

#     return render_template('security/register_user.html', form=form)


# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         # Here you can create a new user with the form data
#         email = form.email.data
#         password = form.password.data
#         user_datastore.create_user(email=email, password=password)
#         db.session.commit()
#         # Redirect to the login page or wherever you want
#         return redirect(url_for('index'))
#     return render_template('security/register_user.html', form=form)

# @auth_bp.route('/register')
# def register():
#     return render_template('security/register_user.html', register_user_form=ExtendedRegisterForm())

# @auth_bp.route('/login')
# def login():
#     return render_template('security/login_user.html', login_user_form=ExtendedLoginForm())

```

## crud_api_calls.py
Path: `/home/milav/code/gppLMSv2/backend/app/routes/crud_api_calls.py`

```py
from flask import Blueprint, render_template, redirect, url_for
from ..forms import BookForm, GenreForm, AuthorForm, UserForm, BookLoanForm, MemberForm
from ..schemas import book_schema, genre_schema, author_schema, user_schema, book_loan_schema, member_schema
import requests

api_call_bp = Blueprint("api_call_bp", __name__)

API_BASE_URL = "http://localhost:5000/api"  # Adjust as needed


# Generalized API call function
def api_call(endpoint, method="get", data=None, id=None, schema=None):
    url = f"{API_BASE_URL}/{endpoint}"
    if id:
        url += f"/{id}"

    if method == "get":
        response = requests.get(url)
    elif method in ["post", "put"]:
        if schema is not None:
            serialized_data = schema.dump(data)
        else:
            serialized_data = data
            print(serialized_data)
        if method == "post":
            response = requests.post(url, json=serialized_data)
        elif method == "put":
            response = requests.put(url, json=serialized_data)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def handle_form_submission(
    form_class,
    schema,
    endpoint,
    template,
    redirect_endpoint,
    list_title,
    edit_title,
    edit_route,
    display_fields,
    id=None,
):
    form = form_class()
    if form.validate_on_submit():
        api_call(
            endpoint,
            method="post" if not id else "put",
            data=form.data,
            id=id,
            schema=schema,
        )
        return redirect(url_for(redirect_endpoint))

    if id:
        item_data = api_call(endpoint, id=id)
        item = schema.load(item_data)
        form = form_class(obj=item)

    items = api_call(endpoint) if not id else None
    return render_template(
        template,
        form=form,
        items=items,
        list_title=list_title,
        edit_title=edit_title,
        edit_route=edit_route,
        display_fields=display_fields,
    )


# Existing book_list function
@api_call_bp.route("/books", methods=["GET", "POST"])
def book_list():
    display_fields = [("title", "isbn_13")]
    return handle_form_submission(
        form_class=BookForm,
        schema=book_schema,
        endpoint="books",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.book_list",
        list_title="Book List",
        edit_title="Edit Book",
        edit_route="api_call_bp.edit_book",
        display_fields=display_fields,
    )


# Edit book function
@api_call_bp.route("/books/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    display_fields = [("title", "isbn_13")]
    return handle_form_submission(
        form_class=BookForm,
        schema=book_schema,
        endpoint="books",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.book_list",
        list_title=None,
        edit_title="Edit Book",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


# Genre list function
@api_call_bp.route("/genres", methods=["GET", "POST"])
def genre_list():
    display_fields = [("name", "description")]
    return handle_form_submission(
        form_class=GenreForm,
        schema=genre_schema,
        endpoint="genres",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.genre_list",
        list_title="Genre List",
        edit_title="Edit Genre",
        edit_route="api_call_bp.edit_genre",
        display_fields=display_fields,
    )


# Edit genre function
@api_call_bp.route("/genres/<int:id>", methods=["GET", "POST"])
def edit_genre(id):
    display_fields = [("name", "description")]
    return handle_form_submission(
        form_class=GenreForm,
        schema=genre_schema,
        endpoint="genres",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.genre_list",
        list_title=None,
        edit_title="Edit Genre",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


# Author list function
@api_call_bp.route("/authors", methods=["GET", "POST"])
def author_list():
    display_fields = [("name", "biography")]
    return handle_form_submission(
        form_class=AuthorForm,
        schema=author_schema,
        endpoint="authors",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.author_list",
        list_title="Author List",
        edit_title="Edit Author",
        edit_route="api_call_bp.edit_author",
        display_fields=display_fields,
    )


# Edit author function
@api_call_bp.route("/authors/<int:id>", methods=["GET", "POST"])
def edit_author(id):
    display_fields = [("name", "biography")]
    return handle_form_submission(
        form_class=AuthorForm,
        schema=author_schema,
        endpoint="authors",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.author_list",
        list_title=None,
        edit_title="Edit Author",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


@api_call_bp.route("/users", methods=["GET", "POST"])
def user_list():
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=UserForm,
        schema=user_schema,
        endpoint="users",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.user_list",
        list_title="User List",
        edit_title="Edit User",
        edit_route="api_call_bp.edit_user",
        display_fields=display_fields,
    )


# Edit user function
@api_call_bp.route("/users/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=UserForm,
        schema=user_schema,
        endpoint="users",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.user_list",
        list_title=None,
        edit_title="Edit User",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )

@api_call_bp.route("/members", methods=["GET", "POST"])
def member_list():
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=MemberForm,
        schema=member_schema,
        endpoint="members",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.member_list",
        list_title="Member List",
        edit_title="Edit Member",
        edit_route="api_call_bp.edit_member",
        display_fields=display_fields,
    )


# Edit member function
@api_call_bp.route("/members/<int:id>", methods=["GET", "POST"])
def edit_member(id):
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=MemberForm,
        schema=member_schema,
        endpoint="members",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.member_list",
        list_title=None,
        edit_title="Edit Member",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


@api_call_bp.route("/bookloans", methods=["GET", "POST"])
def bookloan_list():
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=BookLoanForm,
        schema=book_loan_schema,
        endpoint="bookloans",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.bookloan_list",
        list_title="BookLoan List",
        edit_title="Edit BookLoan",
        edit_route="api_call_bp.edit_bookloan",
        display_fields=display_fields,
    )


# Edit BookLoan function
@api_call_bp.route("/bookloans/<int:id>", methods=["GET", "POST"])
def edit_bookloan(id):
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=BookLoanForm,
        schema=book_loan_schema,
        endpoint="bookloans",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.bookloan_list",
        list_title=None,
        edit_title="Edit BookLoan",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )

```

## __init__.py
Path: `/home/milav/code/gppLMSv2/backend/app/routes/__init__.py`

```py


```

## librarian.py
Path: `/home/milav/code/gppLMSv2/backend/app/routes/librarian.py`

```py
from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_security import current_user
from ..forms import UserForm, BookForm
from ..models import db, user_datastore, User, Role
from ..services import create_book, get_all_books, get_book, update_book

librarian_bp = Blueprint("librarian_bp", __name__)


@librarian_bp.route("/librarian/home")
def home():
    return render_template("librarian/home.html")


@librarian_bp.route("/user/display")
def display_users():
    users = User.query.all()
    return render_template("librarian/user_list.html", users=users)


@librarian_bp.route("/user/show/<int:user_id>")
def show_user(user_id):
    user = user_datastore.find_user(id=user_id)
    if user:
        return render_template("librarian/user_view.html", user=user)
    return {"message": "User not found"}, 404


@librarian_bp.route("/user/add", methods=["GET", "POST"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        # Create a new user with the basic fields
        data = {k: v for k, v in form.data.items() if k not in ["submit", "roles"]}
        user = user_datastore.create_user(**data)

        for role in form.roles.data:
            user.roles.append(role)

        # Commit the new user to the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("librarian_bp.display_users"))

    return render_template("librarian/user_add.html", form=form)


@librarian_bp.route("/user/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))

    # Pre-select the current roles in the form
    form.roles.data = [role for role in user.roles]

    return render_template("librarian/user_edit.html", form=form, user=user)


@librarian_bp.route("/user/delete/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))
    return render_template("librarian/user_delete.html", user=user)


# @librarian_bp.route("/books", methods=["GET", "POST"])
# def book_list():
#     form = BookForm()
#     if form.validate_on_submit():
#         data = {k: v for k, v in form.data.items() if k != "submit"}
#         create_book(data)
#         # new_book = Book(**data)
#         # db.session.add(new_book)
#         # db.session.commit()
#         return redirect(url_for("librarian_bp.book_list"))
#     books = get_all_books()
#     return render_template("book_list.html", form=form, books=books)


# @librarian_bp.route("/books/<int:book_id>", methods=["GET", "POST"])
# def edit_book(book_id):
#     book = get_book(book_id)
#     form = BookForm(obj=book)
#     if form.validate_on_submit():
#         # form.populate_obj(book)
#         # db.session.commit()
#         update_book(book_id, form.data)
#         return redirect(url_for("librarian_bp.book_list"))
#     return render_template("edit_book.html", form=form, book=book)

```

## main.py
Path: `/home/milav/code/gppLMSv2/backend/app/routes/main.py`

```py
from flask import Blueprint, render_template, url_for, redirect
from flask_security import auth_required
from ..forms import RoleSelectForm

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/select_role", methods=["GET", "POST"])
@auth_required("token", "session")
def select_role():
    form = RoleSelectForm()
    if form.validate_on_submit():
        selected_role = form.roles.data
        print(selected_role)
        if selected_role.name == "Librarian":
            return redirect(url_for("librarian_bp.home"))
        elif selected_role.name == "Member":
            return redirect(url_for("member_bp.home"))
    
    return render_template("main/select_role.html", form=form)

```

## member.py
Path: `/home/milav/code/gppLMSv2/backend/app/routes/member.py`

```py
from flask import Blueprint, render_template
from flask_security import auth_required
from ..models import Book
from ..routes.crud_api_calls import api_call

member_bp = Blueprint("member_bp", __name__)

@member_bp.route("/member/home")
@auth_required("token", "session")
def home():
    books = Book.query.all()
    return render_template("member/home.html", books=books)

def request_book(book_id, member_id):
    return api_call(f"books/request/{book_id}/{member_id}", method="post")


def view_loans(member_id):
    return api_call(f"loans/{member_id}", method="get")


def return_book(loan_id):
    return api_call(f"loans/return/{loan_id}", method="put")  

```

## schemas.py
Path: `/home/milav/code/gppLMSv2/backend/app/schemas.py`

```py
from app.extensions import ma
from .extensions import db

from .models import (
    Role,
    User,
    Librarian,
    Member,
    Membership,
    Wishlist,
    Collection,
    Genre,
    Author,
    Book,
    BookLoan,
    Purchase,
    Review,
)


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        sqla_session = db.session


class UserSchema(ma.SQLAlchemyAutoSchema):
    roles = ma.Nested(RoleSchema, many=True, only=["id", "name"])

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        exclude = (
            "fs_uniquifier",
            "password",
        )

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'location')

class LibrarianSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Librarian
        load_instance = True
        sqla_session = db.session


class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True
        sqla_session = db.session        


class MembershipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Membership
        load_instance = True
        sqla_session = db.session

class WishlistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wishlist
        load_instance = True
        sqla_session = db.session

class CollectionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Collection
        load_instance = True
        sqla_session = db.session

class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True
        sqla_session = db.session

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        sqla_session = db.session

class BookLoanSchema(ma.SQLAlchemyAutoSchema):
    # books = ma.Nested("BookSchema", only=["id", "title"])
    # member_id = ma.Nested("MemberSchema", only=["id", "email"])
    class Meta:
        model = BookLoan
        load_instance = True
        sqla_session = db.session
        include_fk = True

class PurchaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Purchase
        load_instance = True
        sqla_session = db.session

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        sqla_session = db.session

class BookSchema(ma.SQLAlchemyAutoSchema):
    authors = ma.Nested(AuthorSchema, many=True, only=["id", "name"])
    genres = ma.Nested(GenreSchema, many=True, only=["id", "name"])
    collections = ma.Nested(CollectionSchema, many=True)
    wishlists = ma.Nested(WishlistSchema, many=True)
    free_access_in_memberships = ma.Nested(MembershipSchema, many=True)
    book_loans = ma.Nested(BookLoanSchema, many=True)
    purchases = ma.Nested(PurchaseSchema, many=True)
    reviews = ma.Nested(ReviewSchema, many=True)

    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)

librarian_schema = LibrarianSchema()
librarians_schema = LibrarianSchema(many=True)

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many=True)

wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)

collections_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

book_loan_schema = BookLoanSchema()
book_loans_schema = BookLoanSchema(many=True)

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

```

## services.py
Path: `/home/milav/code/gppLMSv2/backend/app/services.py`

```py
from .models import db, Book, Genre


def create_book(data):
    Book.create(**data)

def get_all_books():
    return Book.query.all()

def get_book(book_id):
    return Book.query.get(book_id)

def update_book(book_id, data):
    book = Book.query.get(book_id)
    if book:
        book.update(**data)

def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.delete()

      

```

## index.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/admin/index.html`

```html
{% extends 'admin/master.html' %}

{% block body %}
  <p>Hello Admin, Please Login</p>
  <a href="{{ url_for('security.login') }}">{{ 'Login' }}</a>
{% endblock %}

```

## base.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/base.html`

```html
{% extends 'bootstrap/base.html' %}
{% block title %}
    {% if title %}
        {{ title }} - GPP Portal
    {% else %}
        {{ 'Welcome to GPP Portal' }}
    {% endif %}
{% endblock %}
{% block styles %}{{ super() }}{% endblock %}
{% block scripts %}{{ super() }}{% endblock %}
{% block navbar %}
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <button type="button"
                        class="navbar-toggle collapsed"
                        data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1"
                        aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                {% if current_user.is_anonymous %}
                    <a class="navbar-brand" href="{{ url_for("main_bp.index") }}">GPP Portal</a>
                {% else %}
                    <a class="navbar-brand" href="{{ url_for("librarian_bp.home") }}">GPP Portal Home</a>
                {% endif %}
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    {# <li>
                        {% if user.role == 'librarian' %}
                            <a href="{{ url_for("librarian_bp.home") }}">{{ 'Home' }}</a>
                        {% elif user.role == 'member' %}
                            <a href="{{ url_for("member_bp.home") }}">{{ 'Home' }}</a>
                        {% endif %}
                    </li> #}
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    {% if current_user.is_anonymous %}
                        <li>
                            <a href="{{ url_for("security.login") }}">{{ 'Login' }}</a>
                        </li>
                    {% else %}
                        <li>
                            {# <a href="{{ url_for('librarian_bp.display_users') }}">User</a> #}
                            {# <a href="{{ url_for(user.edit_user, user_id=current_user.id) }}">{{ 'User Edit' }}</a> #}
                            {# <a href="{{ url_for('librarian_bp.show_user', user_id=current_user.id) }}">{{ 'User View' }}</a> #}
                            <a href="{{ url_for("security.change_password") }}">{{ 'Update Password' }}</a>
                        </li>
                        <li>
                            <a href="{{ url_for("security.logout") }}">{{ 'Logout' }}</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
{% endblock %}
{% block content %}
    <div class="container">
        {# application content needs to be provided in the app_content block #}
        {% block app_content %}{% endblock %}
    </div>
{% endblock %}

```

## index.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/index.html`

```html
{% extends "base.html" %}
{% block app_content %}
    <h1>Welcome to GPP LMS, Please Login/Register</h1>
    <ul>
        <li>
            <a href="{{ url_for("security.register") }}">User Registration</a>
        </li>
        <li>
            <a href="{{ url_for("security.login") }}">User Login</a>
        </li>
    </ul>
{% endblock %}

```

## edit.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/edit.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ edit_title }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
{% endblock %}

```

## home.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/home.html`

```html
{% extends "base.html" %}
{% block app_content %}
    <h1>Welcome Librarian</h1>
    <ul>
        <li>
            <a href="{{ url_for("api_call_bp.bookloan_list") }}">BookLoan Management</a>
        </li>
        <li>
            <a href="{{ url_for("api_call_bp.user_list") }}">User Management</a>
        </li>
        <li>
            <a href="{{ url_for("api_call_bp.book_list") }}">Book Management</a>
        </li>
        <li>
            <a href="{{ url_for("api_call_bp.genre_list") }}">Genre Management</a>
        </li>
        <li>
            <a href="{{ url_for("api_call_bp.author_list") }}">Author Management</a>
        </li>
    </ul>
{% endblock %}

```

## list.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/list.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ list_title }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
    <ul>
        {% for item in items %}
        <li>
            <a href="{{ url_for(edit_route, id=item.id) }}">
                {% for field_name, label in display_fields %}
                    {{ item[field_name] }}{% if not loop.last %}, {% endif %}
                {% endfor %}
            </a>
        </li>
        {% endfor %}
    </ul>
{% endblock %}

```

## user_add.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/user_add.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ 'Add User' }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
{% endblock %}

```

## user_delete.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/user_delete.html`

```html
{% extends 'base.html' %}
{% block styles %}{{ super() }}{% endblock %}
{% block title %}GPP: Delete User{% endblock %}
{% block app_content %}
    <h1>Delete User</h1>
    <p>Are you sure you want to delete the User "{{ username }}"?</p>
    <form method="POST"
          action="{{ url_for('librarian_bp.delete', user_id=user.id) }}">
        <button type="submit">Delete</button>
    </form>
{% endblock %}

```

## user_edit.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/user_edit.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ 'Edit User' }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
{% endblock %}

```

## user_list.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/user_list.html`

```html
{% extends "base.html" %}
{% block app_content %}
<h1>Manage Users</h1>
<h2><a href="{{ url_for('librarian_bp.add_user') }}">{{ 'Add User' }}</a></h2> <hr/>
    <table class="table table-hover">
        {% for user in users %}
            <tr>
                <td>
                    <p>{{ 'User' }}: {{ user.email }}</p>
                </td>
                <td>
                    <p>
                        <a href="{{ url_for('librarian_bp.show_user', user_id=user.id) }}">{{ 'View User' }}</a> | 
                        <a href="{{ url_for('librarian_bp.edit_user', user_id=user.id) }}">{{ 'Edit User' }}</a> | 
                        <a href="{{ url_for('librarian_bp.delete_user', user_id=user.id) }}">{{ 'Delete User' }}</a>
                    </p>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}

```

## user_view.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/librarian/user_view.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ 'User View' }}</h1>
    <div class="row">
        {% for attr_name, attr_value in user.__dict__.items() %}
            {% if attr_name not in ['_sa_instance_state', 'password', 'confirmed_at', 'fs_uniquifier'] %}
                <p>{{ attr_name }}: {{ attr_value }}</p>
            {% endif %}
        {% endfor %}
    </div>
{% endblock %}

```

## select_role.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/main/select_role.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ 'Select Role' }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
{% endblock %}

```

## books.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/member/books.html`

```html
<!-- books.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Browse Books</h2>
<table>
    <tr>
        <th>Title</th>
        <th>Author</th>
        <th>Status</th>
        <th>Action</th>
    </tr>
    {% for book in books %}
    <tr>
        <td>{{ book.title }}</td>
        <td>{{ book.author }}</td>
        <td>{{ book.status }}</td>
        <td>
            {% if book.status == 'available' %}
            <button onclick="requestBook({{ book.id }}, {{ member_id }})">Request</button>
            {% endif %}
        </td>
    </tr>
    {% endfor %}
</table>

<script>
function requestBook(bookId, memberId) {
    // JavaScript to call the API for requesting a book
}
</script>
{% endblock %}

```

## browse_books.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/member/browse_books.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ 'Book List' }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
    <ul>
        {% for book in books %}
            <li>
                <a href="{{ url_for('api_call_bp.edit_book', book_id=book.id) }}">{{ book.title }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}

```

## browse_genres.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/member/browse_genres.html`

```html
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block app_content %}
    <h1>{{ 'Genre List' }}</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
    <ul>
        {% for genre in genres %}
            <li>
                <a href="{{ url_for('api_call_bp.edit_genre', genre_id=genre.id) }}">{{ genre.name }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}

```

## home.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/member/home.html`

```html
{% extends "base.html" %}
{% block app_content %}
<h1>Welcome Member, Pick your Read..!</h1>
    <table class="table table-hover">
        {% for book in books %}
            <tr>
                <td>
                    <p>{{ 'Book' }}: {{ book.title }}</p>
                </td>
                <td>
                    <p>
                        <a href="{{ url_for('member_bp.home') }}">{{ 'View Book' }}</a> | 
                        <a href="{{ url_for('member_bp.home') }}">{{ 'Loan Request' }}</a> | 
                        <a href="{{ url_for('member_bp.home') }}">{{ 'Buy' }}</a>
                    </p>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}


```

## loans.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/member/loans.html`

```html
<!-- loans.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Your Loans</h2>
<table>
    <tr>
        <th>Title</th>
        <th>Loan Date</th>
        <th>Return</th>
    </tr>
    {% for loan in loans %}
    <tr>
        <td>{{ loan.book.title }}</td>
        <td>{{ loan.loan_date }}</td>
        <td>
            <button onclick="returnBook({{ loan.id }})">Return</button>
        </td>
    </tr>
    {% endfor %}
</table>

<script>
function returnBook(loanId) {
    // JavaScript to call the API for returning a book
}
</script>
{% endblock %}

```

## base.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/base.html`

```html
{# djlint:off H030,H031 #}
{% block doc -%}
<!DOCTYPE html>
<html{% block html_attribs %}{% endblock html_attribs %}>
  {%- block html %}
  <head>
    {%- block head %}
    <title>{% block title %}{{ title|default }}{% endblock title %}</title>

      {%- block metas %}
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
      {%- endblock metas %}

      {%- block head_scripts %}
      {%- endblock head_scripts %}

      {%- block styles %}
        <style>
          .fs-center { text-align: center }
          .fs-important { font-size: larger; font-weight: bold }
          .fs-gap { margin-top: 20px; }
          .fs-div { margin: 4px; }
          .fs-error-msg { color: darkred; }
        </style>
      {%- endblock styles %}
    {%- endblock head %}
  </head>
  <body{% block body_attribs %}{% endblock body_attribs %}>
    {% block body -%}
      {% block navbar %}
      {%- endblock navbar %}
      {% block content -%}
      {%- endblock content %}

      {% block scripts %}
      {%- endblock scripts %}
    {%- endblock body %}
  </body>
  {%- endblock html %}
</html>
{% endblock doc -%}

```

## change_password.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/change_password.html`

```html
{% extends "base.html" %}
{% from "security/_macros.html" import render_field_with_errors, render_field %}

{% block app_content %}
  {% include "security/_messages.html" %}
  <h1>{{ _fsdomain('Change password') }}</h1>
  <form action="{{ url_for_security('change_password') }}" method="post" name="change_password_form">
    {{ change_password_form.hidden_tag() }}
    {% if active_password %}
      {{ render_field_with_errors(change_password_form.password) }}
    {% else %}
      <h3>{{ _fsdomain('You do not currently have a password - this will add one.') }}</h3>
    {% endif %}
    {{ render_field_with_errors(change_password_form.new_password) }}
    {{ render_field_with_errors(change_password_form.new_password_confirm) }}
    {{ render_field(change_password_form.submit) }}
  </form>
{% endblock app_content %}

```

## confirmation_instructions.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/email/confirmation_instructions.html`

```html
{# This template receives the following context:
  confirmation_link - the link that should be fetched (GET) to confirm
  confirmation_token - this token is part of confirmation link - but can be used to
    construct arbitrary URLs for redirecting.
  user - the entire user model object
  security - the Flask-Security configuration
#}
<p>{{ _fsdomain('Please confirm your email through the link below:') }}</p>
<p>
  <a href="{{ confirmation_link }}">{{ _fsdomain('Confirm my account') }}</a>
</p>

```

## reset_instructions.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/email/reset_instructions.html`

```html
{# This template receives the following context:
  reset_link - the link that should be fetched (GET) to reset
  reset_token - this token is part of reset link - but can be used to
    construct arbitrary URLs for redirecting.
  user - the entire user model object
  security - the Flask-Security configuration
#}
<p>
  <a href="{{ reset_link }}">{{ _fsdomain('Click here to reset your password') }}</a>
</p>

```

## reset_notice.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/email/reset_notice.html`

```html
<p>{{ _fsdomain('Your password has been reset') }}</p>

```

## welcome.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/email/welcome.html`

```html
{# This template receives the following context:
  confirmation_link - the link that should be fetched (GET) to confirm
  confirmation_token - this token is part of confirmation link - but can be used to
    construct arbitrary URLs for redirecting.
  user - the entire user model object
  security - the Flask-Security configuration
#}
<p>{{ _fsdomain('Welcome %(email)s!', email=user.email) }}</p>
{% if security.confirmable %}
  <p>{{ _fsdomain('You can confirm your email through the link below:') }}</p>
  <p>
    <a href="{{ confirmation_link }}">{{ _fsdomain('Confirm my account') }}</a>
  </p>
{% endif %}

```

## forgot_password.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/forgot_password.html`

```html
{% extends "base.html" %}
{% from "security/_macros.html" import render_field_with_errors, render_field %}

{% block app_content %}
  {% include "security/_messages.html" %}
  <h1>{{ _fsdomain('Send password reset instructions') }}</h1>
  <form action="{{ url_for_security('forgot_password') }}" method="post" name="forgot_password_form">
    {{ forgot_password_form.hidden_tag() }}
    {{ render_field_with_errors(forgot_password_form.email) }}
    {{ render_field(forgot_password_form.submit) }}
  </form>
  {% include "security/_menu.html" %}
{% endblock app_content %}

```

## login_user.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/login_user.html`

```html
{% extends "base.html" %}
{% from "security/_macros.html" import render_field_with_errors, render_field, render_field_errors, render_form_errors, prop_next %}

{% block app_content %} 
  {% include "security/_messages.html" %}
  <h1>{{ _fsdomain('Login') }}</h1>
  <form action="{{ url_for_security('login') }}{{ prop_next() }}" method="post" name="login_user_form">
    {{ login_user_form.hidden_tag() }}
    {{ render_form_errors(login_user_form) }}
    {% if "email" in identity_attributes %}{{ render_field_with_errors(login_user_form.email) }}{% endif %}
    {% if login_user_form.username and "username" in identity_attributes %}
      {% if "email" in identity_attributes %}<h3>{{ _fsdomain("or") }}</h3>{% endif %}
      {{ render_field_with_errors(login_user_form.username) }}
    {% endif %}
    <div class="fs-gap">{{ render_field_with_errors(login_user_form.password) }}</div>
    {{ render_field_with_errors(login_user_form.remember) }}
    {{ render_field_errors(login_user_form.csrf_token) }}
    {{ render_field(login_user_form.submit) }}
  </form>
  {% if security.webauthn %}
    <hr class="fs-gap">
    <h2>{{ _fsdomain("Use WebAuthn to Sign In") }}</h2>
    <div>
      <form method="get" id="wan_signin_form" name="wan_signin_form">
        <input id="wan_signin" name="wan_signin" type="submit" value="{{ _fsdomain('Sign in with WebAuthn') }}" formaction="{{ url_for_security('wan_signin') }}{{ prop_next() }}">
      </form>
    </div>
  {% endif %}
  {% if security.oauthglue %}
    <hr class="fs-gap">
    <h2>{{ _fsdomain("Use Social Oauth to Sign In") }}</h2>
    {% for provider in security.oauthglue.provider_names %}
      <div class="fs-gap">
        <form method="post" id="{{ provider }}_form" name="{{ provider }}_form">
          <input id="{{ provider }}" name="{{ provider }}" type="submit" value="{{ _fsdomain('Sign in with ')~provider }}" formaction="{{ url_for_security('oauthstart', name=provider) }}{{ prop_next() }}">
          {% if csrf_token is defined %}
            <input id="{{ provider }}_csrf_token" name="{{ provider }}_csrf_token" type="hidden" value="{{ csrf_token() }}">
          {% endif %}
        </form>
      </div>
    {% endfor %}
  {% endif %}
  {% include "security/_menu.html" %}
{% endblock app_content %}

```

## register_user.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/register_user.html`

```html
{% extends "base.html" %}
{% from "security/_macros.html" import render_field_with_errors, render_field, render_form_errors %}
{% block app_content %}
    {% include "security/_messages.html" %}
    <h1>{{ _fsdomain("Register") }}</h1>
    <form action="{{ url_for_security("register") }}"
          method="post"
          name="register_user_form">
        {{ register_user_form.hidden_tag() }}
        {{ render_form_errors(register_user_form) }}
        {{ render_field_with_errors(register_user_form.first_name) }}
        {{ render_field_with_errors(register_user_form.last_name) }}
        {{ render_field_with_errors(register_user_form.username) }}
        {{ render_field_with_errors(register_user_form.email) }}
        {% if security.username_enable %}{{ render_field_with_errors(register_user_form.username) }}{% endif %}
        {{ render_field_with_errors(register_user_form.password) }}
        {% if register_user_form.password_confirm %}
            {{ render_field_with_errors(register_user_form.password_confirm) }}
        {% endif %}
        {{ render_field(register_user_form.submit) }}
    </form>
    {% include "security/_menu.html" %}
{% endblock app_content %}

```

## reset_password.html
Path: `/home/milav/code/gppLMSv2/backend/app/templates/security/reset_password.html`

```html
{% extends "base.html" %}
{% from "security/_macros.html" import render_field_with_errors, render_field %}

{% block app_content %}
  {% include "security/_messages.html" %}
  <h1>{{ _fsdomain('Reset password') }}</h1>
  <form action="{{ url_for_security('reset_password', token=reset_password_token) }}" method="post" name="reset_password_form">
    {{ reset_password_form.hidden_tag() }}
    {{ render_field_with_errors(reset_password_form.password) }}
    {{ render_field_with_errors(reset_password_form.password_confirm) }}
    {{ render_field(reset_password_form.submit) }}
  </form>
  {% include "security/_menu.html" %}
{% endblock app_content %}

```

## views.py
Path: `/home/milav/code/gppLMSv2/backend/app/views.py`

```py
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask import redirect, url_for, request, flash
from .extensions import db
from .models import (
    Role,
    User,
    Librarian,
    Member,
    Membership,
    Wishlist,
    Collection,
    Genre,
    Author,
    Book,
    BookLoan,
    Purchase,
    Review
)


class MyModelView(ModelView):
    # def is_accessible(self):
    #     return current_user.is_active and current_user.is_authenticated and current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("security.login", next=request.url))


class UserView(MyModelView):
    def create_model(self, form):
        try:
            model = self.model()
            form.populate_obj(model)
            model.creator_id = (
                current_user.id
            )  # Set creator_id to the current user's ID
            self.session.add(model)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash("Failed to create record. " + str(ex), "error")
                # log.exception('Failed to create record.')
            self.session.rollback()

            return False
        else:
            self.after_model_change(form, model, True)

        return model


def setup_admin(app):
    # admin = Admin(app, name='GPP Admin', template_mode='bootstrap3')
    admin = Admin(
        app,
        name="GPP FlaskAdmin",
        template_mode="bootstrap3",
        url="/flask-admin",
        endpoint="flask-admin",
    )
    admin.add_view(MyModelView(Role, db.session, category="User"))
    admin.add_view(
        UserView(
            User, db.session, name="User Admin", endpoint="user_admin", category="User"
        )
    )
    admin.add_view(MyModelView(Librarian, db.session, category="User"))
    admin.add_view(MyModelView(Member, db.session, category="User"))
    admin.add_view(MyModelView(Membership, db.session, category="Account"))
    admin.add_view(MyModelView(Wishlist, db.session, category="Account"))
    admin.add_view(MyModelView(Collection, db.session, category="Account"))
    admin.add_view(MyModelView(Genre, db.session, category="BookData"))
    admin.add_view(MyModelView(Author, db.session, category="BookData"))
    admin.add_view(MyModelView(Book, db.session, category="BookData"))
    admin.add_view(MyModelView(BookLoan, db.session, category="Transaction"))
    admin.add_view(MyModelView(Purchase, db.session, category="Transaction"))
    admin.add_view(MyModelView(Review, db.session, category="BookData"))

    return admin

```

## config.py
Path: `/home/milav/code/gppLMSv2/backend/config.py`

```py
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    DEBUG = False
    TESTING = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.googlemail.com"
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 587)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or 1
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "admin@email.com"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "password"


    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SECURITY_PASSWORD_HASH = os.environ.get("SECURITY_PASSWORD_HASH") or "bcrypt"
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT") or "super secret"
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = False
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_TOKEN_AUTHENTICATION_HEADER = None
    SECURITY_POST_LOGIN_VIEW = "/select_role"
    WTF_CSRF_ENABLED = False
    # SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    
    # CELERY_BROKER_URL = "redis://localhost:6379/1"
    # CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    # REDIS_URL = "redis://localhost:6379"
    # CACHE_TYPE = "RedisCache"
    # CACHE_DEFAULT_TIMEOUT = 300
    # CACHE_REDIS_HOST = "localhost"
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_DB = 3    
    
    FLASK_ADMIN_SWATCH = "cerulean"
    
    # CACHE_REDIS_URL = 'redis://localhost:6379/3'
    
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    # ADMINS = ['milav.dabgar@gmail.com']
    # LANGUAGES = ['en', 'es']
    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    
    # OUTH_CLIENT_ID = os.getenv("OUTH_CLIENT_ID")
    # OUTH_CILENT_SECRET = os.getenv("OUTH_CILENT_SECRET")


class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "GPPPortal.sqlite")

    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    # SECURITY_CONFIRMABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_CHANGEABLE = True
    # SECURITY_REGISTER_USER_FORM = "ExtendedRegisterForm"
    # SECURITY_LOGIN_FORM = "ExtendedLoginForm"
    # SECURITY_URL_PREFIX = '/auth'
    # SECURITY_EMAIL_RESET_PASSWORD_TEMPLATE = 'auth/reset_password_instructions.html'

```

## db_migrator.sh
Path: `/home/milav/code/gppLMSv2/backend/db_migrator.sh`

```sh
export FLASK_APP=main.py
# Run migrations
# flask db init
# flask db stamp head
flask db migrate -m "Auto Migrate"
flask db upgrade
# flask db downgrade

```

## local_gunicorn.sh
Path: `/home/milav/code/gppLMSv2/backend/local_gunicorn.sh`

```sh
#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"
if [ -d ".venv" ];
then
    echo "Enabling virtual env"
else
    echo "No Virtual env. Please run setup.sh first"
    exit N
fi

# Activate virtual env
. .venv/bin/activate
export ENV=stage
gunicorn main:app --worker-class gevent --bind 127.0.0.1:8000 --workers=4
deactivate



```

## local_mailhog.sh
Path: `/home/milav/code/gppLMSv2/backend/local_mailhog.sh`

```sh
#! /usr/bin/bash

echo "======================================================================"
echo "Welcome to the local run for the backend of Kanban Application."
echo "This application has been created by Sayantan Das as a part of the MAD II Project. He can be contacted at 21f1002905@student.onlinedegree.iitm.ac.in."
echo "This will start the Mail-Hog Server for the testing of E-mail automation." 
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"
if [ -d ".venv" ];
then
    echo "Enabling virtual env"
else
    echo "No Virtual env. Please run setup.sh first"
    exit N
fi


~/go/bin/MailHog

```

## local_run.sh
Path: `/home/milav/code/gppLMSv2/backend/local_run.sh`

```sh
#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"
if [ -d ".venv" ];
then
    echo "Enabling virtual env"
else
    echo "No Virtual env. Please run setup.sh first"
    exit N
fi

# Activate virtual env
. .venv/bin/activate
export ENV=LocalDevelopmentConfig
python main.py
deactivate

```

## local_setup.sh
Path: `/home/milav/code/gppLMSv2/backend/local_setup.sh`

```sh
#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"

if [ -d ".venv" ];
then
    echo ".venv folder exists. Installing using pip"
else
    echo "creating .pyvenv and install using pip"
    python -m venv .venv
fi

# Activate virtual env
. .venv/bin/activate

# Upgrade the PIP
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=main.py
# flask db init
# Work done. so deactivate the virtual env
deactivate

```

## local_testing.sh
Path: `/home/milav/code/gppLMSv2/backend/local_testing.sh`

```sh
#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"
if [ -d ".venv" ];
then
    echo "Enabling virtual env"
else
    echo "No Virtual env. Please run setup.sh first"
    exit N
fi

# Activate virtual env
. .venv/bin/activate
export ENV=testing
export FLASK_APP=main.py
# Run migrations
flask db init
flask db stamp head
flask db migrate -m "Temporary migration message"
flask db upgrade

# pytest --verbose --disable-warnings -s
deactivate

```

## main.py
Path: `/home/milav/code/gppLMSv2/backend/main.py`

```py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

```

## babel.config.js
Path: `/home/milav/code/gppLMSv2/frontend/babel.config.js`

```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ]
}

```

## index.html
Path: `/home/milav/code/gppLMSv2/frontend/public/index.html`

```html
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>

```

## App.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/App.vue`

```vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/librarian/home">LibrarianDashboardView</router-link> |
      <router-link to="/member/home">MemberDashboardView</router-link>
    </nav>
    <nav>
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/logout">Logout</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

```

## axiosConfig.js
Path: `/home/milav/code/gppLMSv2/frontend/src/axiosConfig.js`

```js
import axios from "axios";

// Create an Axios instance
const axiosInstance = axios.create({
  baseURL: "http://localhost:5000/",
});

// Request Interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("authToken");
    if (token) {
      config.headers["Authentication-Token"] = token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;

```

## ChangePassword.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/auth/ChangePassword.vue`

```vue
<template>
  <div>
    <h2>Change Password</h2>
    <form @submit.prevent="changePassword">
      <input type="password" v-model="password" placeholder="Current Password" required />
      <input type="password" v-model="newPassword" placeholder="New Password" required />
      <input type="password" v-model="newPasswordConfirm" placeholder="Confirm New Password" required />
      <button type="submit">Change Password</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import config from "@/config";
const apiBaseUrl = config.apiBaseUrl;

export default {
  data() {
    return {
      password: '',
      newPassword: '',
      newPasswordConfirm: ''
    };
  },
  methods: {
    async changePassword() {
      try {
        const authToken = localStorage.getItem('authToken');
        const response = await axios.post(`${apiBaseUrl}/lchange`, {
          password: this.password,
          new_password: this.newPassword,
          new_password_confirm: this.newPasswordConfirm
        }, {
          headers: {
            'Authentication-Token': authToken
          }
        });
        console.log(response.data);
        this.$router.push('/login');
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

```

## ForgotPassword.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/auth/ForgotPassword.vue`

```vue
<template>
  <div>
    <h2>Forgot Password</h2>
    <form @submit.prevent="submitEmail">
      <input type="email" v-model="email" placeholder="Enter your email" required />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import config from "@/config";
const apiBaseUrl = config.apiBaseUrl;

export default {
  data() {
    return {
      email: ''
    };
  },
  methods: {
    async submitEmail() {
      try {
        const response = await axios.post(`${apiBaseUrl}/reset`, {
          email: this.email
        });
        console.log(response.data);
        // Handle success (show message, redirect, etc.)
        alert('Reset link sent to mail');
        this.$router.push('/login');
      } catch (error) {
        console.error(error);
        alert('Password Reset failed!');
      }
    }
  }
};
</script>

```

## ProfileComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/auth/ProfileComponent.vue`

```vue
<template>
    <div>
      <h2>My Profile</h2>
      <input type="text" v-model="firstName">
      <input type="text" v-model="lastName"> 
      <button @click="saveProfile">Save Changes</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios' 
  
  export default {
    data() {
      return {
        firstName: '',
        lastName: '',
        // ... other profile data
      }
    },
    created() {
      this.fetchProfile()
    },
    methods: {
      async fetchProfile() {
        const response = await axios.get('/profile')
        // Populate this.firstName, this.lastName, etc. from response.data
      },
      async saveProfile() {
        const updatedData = { 
           firstName: this.firstName,
           lastName: this.lastName,
           // ... other changed data
        } 
        await axios.put('/profile', updatedData)
        // Display success message 
      }
    }
  }
  </script>
  

```

## UserLogin.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/auth/UserLogin.vue`

```vue
<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="submitLogin">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="credentials.email" required />
      </div>

      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="credentials.password" required />
      </div>

      <div>
        <label for="remember">Remember me</label>
        <input type="checkbox" id="remember" v-model="credentials.remember" />
      </div>

      <button type="submit">Login</button>
    </form>
    <p>
      Don't have an account? <router-link to="/register">Register</router-link>
    </p>
    <p>Forgot password? <router-link to="/reset">Reset</router-link></p>
    <p>Change password: <router-link to="/change">Change</router-link></p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      credentials: { email: "", password: "", remember: false },
    };
  },
  methods: {
    async submitLogin() {
      try {
        await this.$store.dispatch("login", this.credentials);
        this.$router.push("/select-role");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

```

## UserLogout.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/auth/UserLogout.vue`

```vue
<template>
  <div>
    <button @click="submitLogout">Logout</button>
  </div>
</template>

<script>
export default {
  methods: {
    async submitLogout() {
      try {
        await this.$store.dispatch("logout");
        this.$router.push("/login");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

```

## UserRegistration.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/auth/UserRegistration.vue`

```vue
<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="submitRegister">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="credentials.email" required />
      </div>

      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="credentials.password" required />
      </div>

      <button type="submit">Register</button>
    </form>

    <p>Already have an account? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      credentials: { email: "", password: "" },
    };
  },
  methods: {
    async submitRegister() {
      try {
        await this.$store.dispatch("register", this.credentials);
        this.$router.push("/select-role");
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

```

## BrowseBooks.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookBrowsing/BrowseBooks.vue`

```vue
<!-- src/components/BookBrowsing/BrowseBooks.vue -->
<template>
  <div class="browse-books">
  <div class="controls">
    <input v-model="searchQuery" type="text" placeholder="Search books..." class="search-input" />
    <select v-model="sortOption" class="sort-select">
      <option value="">Sort by...</option>
      <option value="title-asc">Title (A-Z)</option>
      <option value="title-desc">Title (Z-A)</option>
      <option value="rating-asc">Rating (Low to High)</option>
      <option value="rating-desc">Rating (High to Low)</option>
    </select>
    <button @click="showFilters = !showFilters" class="filter-toggle">
      {{ showFilters ? 'Hide Filters' : 'Show Filters' }}
    </button>
  </div>

  <div class="filters-and-books">
    <div class="side-pane">
      <SideMenu v-if="showFilters" :is-open="showFilters" @toggle="showFilters = !showFilters"
        @filter-changed="onFilterChanged" />
    </div>
    <div class="book-list">
      <CardComponent v-for="book in filteredBooks" :key="book.id" :title="book.title"
        :subtitle="book.authors.map(author => author.name).join(', ')" :description="`Rating: ${book.rating}`"
        :image="book.coverImage">
        <button @click="requestLoan(book.id)">Request</button>
      </CardComponent>
    </div>
  </div>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';
import SideMenu from './SideMenu.vue';
import CardComponent from './CardComponent.vue';
import filterBooks from '@/utils/filterBooks';

export default {
  components: {
    SideMenu,
    CardComponent,
  },
  data() {
    return {
      books: [],
      searchQuery: '',
      sortOption: '',
      showFilters: false,
      selectedFilters: {
        genres: [],
        authors: [],
        languages: [],
        ratings: [],
        types: [],
        publishers: [],
        publicationDates: [],
        freeAccessInMemberships: [],
        collections: [],
        wishlists: [],
      },
    };
  },
  async created() {
    this.books = await bookService.getAll();
  },
  computed: {
    filteredBooks() {
      let filtered = filterBooks(this.books, this.searchQuery, this.selectedFilters);

      if (this.sortOption) {
        const [sortBy, sortOrder] = this.sortOption.split('-');
        filtered.sort((a, b) => {
          let comparison = 0;
          if (sortBy === 'title') {
            comparison = a.title.localeCompare(b.title);
          } else if (sortBy === 'rating') {
            comparison = a.rating - b.rating;
          }
          return sortOrder === 'asc' ? comparison : -comparison;
        });
      }

      return filtered;
    },
  },
  methods: {
    async requestLoan(bookId) {
      try {
        await bookLoanService.requestLoan(bookId, this.$store.state.user.id);
        this.$emit('loan-created');
      } catch (error) {
        console.error(error);
      }
    },
    onFilterChanged(filters) {
      this.selectedFilters = { ...this.selectedFilters, ...filters };
    },
  },
};
</script>

<style scoped>

.browse-books {
  flex: 1;
  padding: 10px;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 10px;
}

.filters-and-books {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 20px;
}

.side-pane {
  border-right: 1px solid #ccc;
  overflow-y: auto;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  justify-content: start;
}

.card {
  width: 200px; 
  height: 300px; 
}

.controls {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.search-input {
  flex: 1;
  padding: 5px;
  margin-right: 10px;
}

.sort-select {
  margin-right: 10px;
}
</style>

```

## BrowseGenre.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookBrowsing/BrowseGenre.vue`

```vue
<!-- src/components/BookBrowsing/BrowseGenre.vue -->
<template>
    <div class="browse-genre">
      <h2>Browse Genres</h2>
      <div class="controls">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search genres..."
          class="search-input"
        />
        <select v-model="sortOption" class="sort-select">
          <option value="">Sort by...</option>
          <option value="name-asc">Name (A-Z)</option>
          <option value="name-desc">Name (Z-A)</option>
        </select>
      </div>
      <div class="genre-list">
        <CardComponent
          v-for="genre in filteredGenres"
          :key="genre.id"
          :title="genre.name"
          @click="selectGenre(genre)"
          :class="{ selected: selectedGenre && selectedGenre.id === genre.id }"
        />
      </div>
    </div>
  </template>
  
  <script>
  import { genreService } from '@/services/ApiService';
  import CardComponent from './CardComponent';
  
  export default {
    components: {
      CardComponent,
    },
    data() {
      return {
        genres: [],
        searchQuery: '',
        sortOption: '',
        selectedGenre: null,
      };
    },
    computed: {
      filteredGenres() {
        let filtered = this.genres.filter((genre) =>
          genre.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
  
        if (this.sortOption) {
          const [sortBy, sortOrder] = this.sortOption.split('-');
          filtered.sort((a, b) => {
            let comparison = 0;
            if (sortBy === 'name') {
              comparison = a.name.localeCompare(b.name);
            }
            return sortOrder === 'asc' ? comparison : -comparison;
          });
        }
  
        return filtered;
      },
    },
    methods: {
      async fetchGenres() {
        this.genres = await genreService.getAll();
      },
      selectGenre(genre) {
        this.selectedGenre = genre;
        this.$emit('genre-selected', genre);
      },
    },
    created() {
      this.fetchGenres();
    },
  };
  </script>
  
  <style scoped>
  .browse-genre {
    margin-bottom: 20px;
  }
  
  .controls {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .search-input {
    flex: 1;
    padding: 5px;
    margin-right: 10px;
  }
  
  .sort-select {
    margin-right: 10px;
  }
  
  .genre-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
  }
  
  .genre-list .card {
    cursor: pointer;
  }
  
  .genre-list .card.selected {
    background-color: #f0f0f0;
  }
  </style>./CardComponent.vue

```

## CardComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookBrowsing/CardComponent.vue`

```vue
<!-- src/components/BookBrowsing/CardComponent -->
<template>
    <div class="card">
      <img :src="image" alt="Card Image" class="card-image" />
      <div class="card-content">
        <h3 class="card-title">{{ title }}</h3>
        <p class="card-subtitle">{{ subtitle }}</p>
        <p class="card-description">{{ description }}</p>
        <div class="card-actions">
          <slot></slot>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      subtitle: String,
      description: String,
      image: String,
    },
  };
  </script>
  
  <style scoped>
  .card {
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  
  .card-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  
  .card-content {
    padding: 16px;
  }
  
  .card-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .card-subtitle {
    font-size: 14px;
    color: #666;
    margin-bottom: 8px;
  }
  
  .card-description {
    font-size: 14px;
    margin-bottom: 16px;
  }
  
  .card-actions {
    display: flex;
    justify-content: flex-end;
  }
  </style>

```

## FilterSection.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookBrowsing/FilterSection.vue`

```vue
<!-- src/components/BookBrowsing/FilterSection.vue -->
<template>
    <div class="filter-section">
      <h3>{{ title }}</h3>
      <div v-for="option in options" :key="option.id || option">
        <label>
          <input
            type="checkbox"
            :value="option.id || option"
            v-model="selectedOptions"
            @change="onFilterChanged"
          />
          {{ option.name || option }}
        </label>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      options: Array,
    },
    data() {
      return {
        selectedOptions: [],
      };
    },
    methods: {
      onFilterChanged() {
        this.$emit('filter-changed', this.selectedOptions);
      },
    },
  };
  </script>
  
  <style scoped>
  .filter-section {
    margin-bottom: 10px;
  }
  </style>

```

## SideMenu.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookBrowsing/SideMenu.vue`

```vue
<!-- src/components/BookBrowsing/SideMenu.vue -->
<template>
    <div class="side-menu" :class="{ open: isOpen }">
      <button
        class="toggle-button"
        @click="toggleMenu"
        aria-label="Toggle menu"
        aria-expanded="isOpen"
        aria-controls="side-menu-body"
      >
        <span class="line" :class="{ open: isOpen }"></span>
        <span class="line" :class="{ open: isOpen }"></span>
        <span class="line" :class="{ open: isOpen }"></span>
      </button>
  
      <transition name="slide">
        <div v-if="isOpen" id="side-menu-body" class="side-menu-body">
          <FilterSection
            v-for="filterType in filterTypes"
            :key="filterType"
            :title="filterType"
            :options="filters[filterType]"
            @filter-changed="onFilterChanged(filterType, $event)"
          />
        </div>
      </transition>
    </div>
  </template>
  
  <script>
  import FilterSection from './FilterSection.vue';
  import { genreService, authorService, bookService } from '@/services/ApiService';
  
  export default {
    components: {
      FilterSection,
    },
    props: {
      isOpen: Boolean,
    },
    data() {
      return {
        filters: {},
        selectedFilters: {},
        isLoading: true,
        isError: false,
      };
    },
    async created() {
      try {
        const filters = await this.fetchFilters();
        this.filters = filters;
        this.selectedFilters = this.initializeSelectedFilters();
      } catch (error) {
        console.error(error);
        this.isError = true;
      } finally {
        this.isLoading = false;
      }
    },
    computed: {
      filterTypes() {
        return Object.keys(this.filters);
      },
    },
    methods: {
      async fetchFilters() {
        const [genres, authors, books] = await Promise.all([
          genreService.getAll(),
          authorService.getAll(),
          bookService.getAll(),
        ]);
  
        const distinctBookValues = new Map();
        books.forEach((book) => {
          for (const field of [
            'language',
            'type',
            'publisher',
            'publication_date',
            'free_access_in_memberships',
            'collections',
            'wishlists',
          ]) {
            const value = book[field];
            if (value !== null) {
              const set = distinctBookValues.get(field) || new Set();
              set.add(value);
              distinctBookValues.set(field, set);
            }
          }
        });
  
        return {
          genres,
          authors,
          languages: [...distinctBookValues.get('language')],
          ratings: [5, 4, 3, 2, 1],
          types: [...distinctBookValues.get('type')],
          publishers: [...distinctBookValues.get('publisher')],
          publicationDates: [...distinctBookValues.get('publication_date')],
          freeAccessInMemberships: [...distinctBookValues.get('free_access_in_memberships')],
          collections: [...distinctBookValues.get('collections')],
          wishlists: [...distinctBookValues.get('wishlists')],
        };
      },
      initializeSelectedFilters() {
        return Object.fromEntries(Object.keys(this.filters).map((key) => [key, []]));
      },
      onFilterChanged(filterType, selectedOptions) {
        this.selectedFilters[filterType] = selectedOptions;
        this.$emit('filter-changed', this.selectedFilters);
      },
      toggleMenu() {
        this.$emit('toggle');
      },
    },
  };
  </script>
  
  <style scoped>
.side-menu {
  position: relative;
  width: 40px;
  background-color: #f0f0f0;
  transition: width 0.3s;
  overflow: hidden;
}

.side-menu.open {
  width: 300px;
}

.toggle-button {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 30px;
  height: 24px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  z-index: 1;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.line {
  width: 100%;
  height: 3px;
  background-color: #333;
  transition: transform 0.3s, width 0.3s;
}

.line.open:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.line.open:nth-child(2) {
  transform: scaleX(0);
}

.line.open:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

.side-menu-body {
  padding: 10px;
  padding-left: 50px; /* Adjust this value to give space for the hamburger button */
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}
</style>

```

## BookLoanDetailsComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookLoanDetailsComponent.vue`

```vue
<template>
  <div class="book-loan-details">
    <h2>Loan Details</h2>
    <div>
      <h3>ID: {{ loanDetails.id }}</h3>
      <p>Book ID : {{ loanDetails.book_id }}</p>
      <p>Member ID: {{ loanDetails.member_id }}</p>
      <p>Loan Date: {{ loanDetails.loan_date }}</p>
      <p>Due Date: {{ loanDetails.due_date }}</p>
      <p>Status: {{ loanDetails.status }}</p>
    </div>
    <form @submit.prevent="updateLoanDetails">
      <select v-model="loanDetails.status">
        <option>requested</option>
        <option>approved</option>
      </select>
      <button type="submit">Update Loan</button>
    </form>
  </div>
</template>

<script>
import { bookLoanService } from "@/services/ApiService";

export default {
  computed: {
    loanId() {
      return this.$route.params.id;
    }
  },
  data() {
    return {
      loanDetails: {},
    };
  },
  created() {
    this.fetchLoanDetails();
  },
  methods: {
    async fetchLoanDetails() {
      this.loanDetails = await bookLoanService.getById(this.loanId);
    },
    async updateLoanDetails() {
      await bookLoanService.update(this.loanId, this.loanDetails);
    },
  },
};
</script>

<style scoped>
/* Your CSS here */
</style>

```

## BookLoanRequestComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookLoanRequestComponent.vue`

```vue
<template>
  <div>
    <h2>Request a Book Loan</h2>
    <form @submit.prevent="requestLoan">
      <label for="book">Book:</label>
      <select v-model="selectedBookId">
        <option v-for="book in books" :key="book.id" :value="book.id">
          {{ book.title }}
        </option>
      </select>
      <button type="submit">Request Loan</button>
    </form>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      books: [],
      selectedBookId: null
    }
  },

  async created() {
    try {
      this.books = await bookService.getAll();
    } catch (error) {
      console.error(error);
    }
  },

  methods: {
    async requestLoan() {
      try {
        await bookLoanService.requestLoan(this.selectedBookId, this.$store.state.user.id);
        this.selectedBookId = null;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>

```

## BookLoanRequestsListComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookLoanRequestsListComponent.vue`

```vue
<template>
  <div class="book-loan-requests">
    <h2>Loan Requests</h2>
    <table>
      <thead>
        <tr>
          <th>Loan ID</th>
          <th>Member ID</th>
          <th>Book Title</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="loan in loans" :key="loan.id">
          <td>{{ loan.id }}</td>
          <td>{{ loan.member_id }}</td>
          <td>{{ loan.bookTitle }}</td>
          <td>{{ loan.status }}</td>
          <td>
            <button @click="handleLoanAction(loan.id, 'approve')">Approve</button>
            <button @click="handleLoanAction(loan.id, 'reject')">Reject</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      loans: []
    }
  },

  async created() {
    await this.fetchLoans();
  },

  methods: {
    async fetchLoans() {
      const filter = { status: 'requested' };
      this.loans = await bookLoanService.fetchLoans(filter);
    },

    async handleLoanAction(id, action) {
      if (action === 'approve') {
        await bookLoanService.approveLoan(id);
      } else if (action === 'reject') {
        await bookLoanService.delete(id);
      }
      await this.fetchLoans();
    }
  }
}
</script>

```

## BookLoansListComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BookLoansListComponent.vue`

```vue
<template>
  <div class="book-loan-lists">
    <h2>Book Loans</h2>
    <table>
      <thead>
        <tr>
          <th>Loan ID</th>
          <th>Member ID</th>
          <th>Book Title</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="loan in loans" :key="loan.id">
          <td>{{ loan.id }}</td>
          <td>{{ loan.member_id }}</td>
          <td>{{ loan.bookTitle }}</td>
          <td>{{ loan.status }}</td>
          <td>
            <router-link :to="{ name: 'LoanDetails', params: { id: loan.id } }">View Details</router-link>|
            <button @click="handleReturnLoan(loan.id)" :disabled="loan.status !== 'approved'">
              Return Loan
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { bookLoanService } from "@/services/ApiService";

export default {
  props: ["memberId"],

  data() {
    return {
      loans: [],
    };
  },

  async created() {
    this.loans = await bookLoanService.fetchLoans();
  },

  methods: {
    async handleReturnLoan(loanId) {
      await bookLoanService.returnLoan(loanId);
      this.loans = await bookLoanService.fetchLoans(); // Refresh the list of loans
    },
  },
};
</script>

```

## BrowseBooks.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BrowseBooks.vue`

```vue
<template>
  <div class="browse-books">
    <h2>Browse Books</h2>
    <div class="controls">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search books..."
        class="search-input"
      />
      <select v-model="sortOption" class="sort-select">
        <option value="">Sort by...</option>
        <option value="title-asc">Title (A-Z)</option>
        <option value="title-desc">Title (Z-A)</option>
        <option value="rating-asc">Rating (Low to High)</option>
        <option value="rating-desc">Rating (High to Low)</option>
      </select>
      <button @click="showFilters = !showFilters" class="filter-toggle">
        {{ showFilters ? 'Hide Filters' : 'Show Filters' }}
      </button>
    </div>
    <div v-if="showFilters" class="filters">
      <div v-for="(options, filterType) in filters" :key="filterType" class="filter">
        <h3>{{ filterType }}</h3>
        <div v-for="option in options" :key="option.id" class="filter-option">
          <input
            type="checkbox"
            :id="option.id"
            :value="option.id"
            v-model="selectedFilters[filterType]"
          />
          <label :for="option.id">{{ option.name || option }}</label>
        </div>
      </div>
    </div>
    <div class="book-list">
      <div v-for="book in filteredBooks" :key="book.id" class="book-item">
        <img :src="book.coverImage" alt="Book Cover" class="book-cover" />
        <div class="book-details">
          <h3>{{ book.title }}</h3>
          <p>{{ book.authors.map(author => author.name).join(', ') }}</p>
          <p>Rating: {{ book.rating }}</p>
          <button @click="requestLoan(book.id)">Request</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      books: [],
      searchQuery: '',
      sortOption: '',
      showFilters: false,
      filters: {
        genres: [],
        authors: [],
        languages: [],
        ratings: [],
        types: [],
        publishers: [],
        publicationDates: [],
        freeAccessInMemberships: [],
        collections: [],
        wishlists: [],
      },
      selectedFilters: {
        genres: [],
        authors: [],
        languages: [],
        ratings: [],
        types: [],
        publishers: [],
        publicationDates: [],
        freeAccessInMemberships: [],
        collections: [],
        wishlists: [],
      },
    };
  },
  async created() {
    this.books = await bookService.getAll();
    this.populateFilters();
  },
  computed: {
    filteredBooks() {
      let filtered = this.books.filter(book => {
        const matchesQuery = !this.searchQuery || book.title.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesFilters = Object.keys(this.selectedFilters).every(filterType => {
          const filterOptions = this.selectedFilters[filterType];
          if (filterOptions.length === 0) return true;
          if (filterType === 'genres') {
            return book.genres.some(genre => filterOptions.includes(genre.id));
          } else if (filterType === 'authors') {
            return book.authors.some(author => filterOptions.includes(author.id));
          } else if (filterType === 'freeAccessInMemberships') {
            return book.free_access_in_memberships.some(membership => filterOptions.includes(membership.id));
          } else if (filterType === 'collections') {
            return book.collections.some(collection => filterOptions.includes(collection.id));
          } else if (filterType === 'wishlists') {
            return book.wishlists.some(wishlist => filterOptions.includes(wishlist.id));
          } else {
            return filterOptions.includes(book[filterType]);
          }
        });
        return matchesQuery && matchesFilters;
      });

      if (this.sortOption) {
        const [sortBy, sortOrder] = this.sortOption.split('-');
        filtered.sort((a, b) => {
          let comparison = 0;
          if (sortBy === 'title') {
            comparison = a.title.localeCompare(b.title);
          } else if (sortBy === 'rating') {
            comparison = a.rating - b.rating;
          }
          return sortOrder === 'asc' ? comparison : -comparison;
        });
      }

      return filtered;
    },
  },
  methods: {
    async requestLoan(bookId) {
      try {
        await bookLoanService.requestLoan(bookId, this.$store.state.user.id);
        this.$emit('loan-created');
      } catch (error) {
        console.error(error);
      }
    },
    populateFilters() {
      this.filters.genres = [...new Set(this.books.flatMap(book => book.genres))].map(genre => ({ id: genre.id, name: genre.name }));
      this.filters.authors = [...new Set(this.books.flatMap(book => book.authors))].map(author => ({ id: author.id, name: author.name }));
      this.filters.languages = [...new Set(this.books.map(book => book.language))];
      this.filters.ratings = [...new Set(this.books.map(book => book.rating))];
      this.filters.types = [...new Set(this.books.map(book => book.type))];
      this.filters.publishers = [...new Set(this.books.map(book => book.publisher))];
      this.filters.publicationDates = [...new Set(this.books.map(book => book.publication_date))];
      this.filters.freeAccessInMemberships = [...new Set(this.books.flatMap(book => book.free_access_in_memberships))].map(membership => ({ id: membership.id, name: membership.name }));
      this.filters.collections = [...new Set(this.books.flatMap(book => book.collections))].map(collection => ({ id: collection.id, name: collection.name }));
      this.filters.wishlists = [...new Set(this.books.flatMap(book => book.wishlists))].map(wishlist => ({ id: wishlist.id, name: wishlist.name }));
    },
  },
};
</script>

<style scoped>
.browse-books {
  flex: 1;
  padding: 10px;
}

.controls {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.search-input {
  flex: 1;
  padding: 5px;
  margin-right: 10px;
}

.sort-select {
  margin-right: 10px;
}

.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
}

.filter {
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.filter-option {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.filter-option input {
  margin-right: 5px;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.book-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.book-cover {
  width: 150px;
  height: 200px;
  object-fit: cover;
  margin-bottom: 10px;
}

.book-details {
  flex: 1;
}
</style>

```

## BrowseGenres.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BrowseGenres.vue`

```vue
<template>
  <div>
    <h1>Genres</h1>
    <ul>
      <li v-for="genre in genres" :key="genre.id" @click="selectGenre(genre.id)">
        {{ genre.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { genreService } from '@/services/ApiService';

export default {
  data() {
    return {
      genres: [],
    };  
  },
  async created() {
    try {
      this.genres = await genreService.getAll();
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    selectGenre(genreId) {
      this.$emit('genre-selected', genreId);
    },
  },
};
</script>

```

## BrowseGenre.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/BrowseGenre.vue`

```vue
<template>
  <div class="browse-genre">
    <h2>Browse Genres</h2>
    <div class="controls">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search genres..."
        class="search-input"
      />
      <select v-model="sortOption" class="sort-select">
        <option value="">Sort by...</option>
        <option value="name-asc">Name (A-Z)</option>
        <option value="name-desc">Name (Z-A)</option>
      </select>
    </div>
    <ul>
      <li
        v-for="genre in filteredGenres"
        :key="genre.id"
        @click="selectGenre(genre)"
        :class="{ selected: selectedGenre && selectedGenre.id === genre.id }"
      >
        {{ genre.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { genreService } from '@/services/ApiService';

export default {
  data() {
    return {
      genres: [],
      searchQuery: '',
      sortOption: '',
      selectedGenre: null,
    };
  },
  computed: {
    filteredGenres() {
      let filtered = this.genres.filter(genre =>
        genre.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );

      if (this.sortOption) {
        const [sortBy, sortOrder] = this.sortOption.split('-');
        filtered.sort((a, b) => {
          let comparison = 0;
          if (sortBy === 'name') {
            comparison = a.name.localeCompare(b.name);
          }
          return sortOrder === 'asc' ? comparison : -comparison;
        });
      }

      return filtered;
    },
  },
  methods: {
    async fetchGenres() {
      this.genres = await genreService.getAll();
    },
    selectGenre(genre) {
      this.selectedGenre = genre;
      this.$emit('genre-selected', genre);
    },
  },
  created() {
    this.fetchGenres();
  },
};
</script>

<style scoped>
.browse-genre {
  margin-bottom: 20px;
}

.controls {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.search-input {
  flex: 1;
  padding: 5px;
  margin-right: 10px;
}

.sort-select {
  margin-right: 10px;
}

.browse-genre ul {
  list-style-type: none;
  padding: 0;
}

.browse-genre li {
  cursor: pointer;
  padding: 5px;
}

.browse-genre li:hover,
.browse-genre li.selected {
  background-color: #f0f0f0;
}
</style>

```

## FilterSection.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/FilterSection.vue`

```vue
<template>
    <div class="filter-section">
      <h3>{{ title }}</h3>
      <div v-for="option in options" :key="option.id || option">
        <label>
          <input type="checkbox" :value="option.id || option" v-model="selectedOptions" @change="onFilterChanged">
          {{ option.name || option }}
        </label>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      options: Array,
    },
    data() {
      return {
        selectedOptions: [],
      };
    },
    methods: {
      onFilterChanged() {
        this.$emit('filter-changed', this.selectedOptions);
      },
    },
  };
  </script>
  
  <style scoped>
  .filter-section {
    margin-bottom: 10px;
  }
  </style>

```

## GeneralEdit.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/GeneralEdit.vue`

```vue
<template>
  <div>
    <h1>Edit {{ type }}</h1>
    <form @submit.prevent="submitForm">
      <div v-for="(value, key) in formData" :key="key">
        <label :for="key">{{ capitalizeFirstLetter(key) }}</label>
        <input v-model="formData[key]" :id="key" type="text" />
      </div>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    type: String,
    id: [String, Number],
  },
  data() {
    return {
      formData: {},
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios
        .get(`http://localhost:5000/api/${this.type.toLowerCase()}s/${this.id}`)
        .then((response) => {
          this.formData = response.data;
        });
    },
    submitForm() {
      axios
        .put(
          `http://localhost:5000/api/${this.type.toLowerCase()}s/${this.id}`,
          this.formData
        )
        .then(() => {
          this.$router.push(`/${this.type.toLowerCase()}s`);
        });
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
  },
};
</script>

```

## GeneralList.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/GeneralList.vue`

```vue
<template>
    <div>
        <ul>
            <h1>{{ title }}</h1>
            <li v-for="item in items" :key="item.id">
                <router-link :to="{ name: editRoute, params: { id: item.id } }">
                    {{ item.displayText }}
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import { userService, authorService, genreService, bookService } from "@/services/ApiService";

const serviceMap = {
    users: userService,
    authors: authorService,
    genres: genreService,
    books: bookService,
};

export default {
    props: {
        resourceType: {
            type: String,
            required: true,
        },
        editRoute: {
            type: String,
            required: true,
        },
    },

    data() {
        return {
            items: [],
            title: "",
        };
    },

    created() {
        this.fetchData();
    },

    watch: {
        "$route.params": {
            handler() {
                this.fetchData();
            },
            immediate: true,
        },
    },

    methods: {
        async fetchData() {
            try {
                const service = serviceMap[this.resourceType];
                const data = await service.getAll();
                this.items = data.map((item) => ({
                    id: item.id,
                    displayText: item.title || item.name || item.email,
                }));
                this.title = this.resourceType.charAt(0).toUpperCase() + this.resourceType.slice(1);
            } catch (error) {
                console.error(error);
            }
        },
    },
};
</script>

```

## RoleSelectionComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/RoleSelectionComponent.vue`

```vue
<template>
  <div class="role-selection">
    <h2>Select Your Role</h2>
    <button @click="selectRole('member')">Member</button>
    <button @click="selectRole('librarian')">Librarian</button>
  </div>
</template>

<script>
export default {
  methods: {
    selectRole(role) {
      this.$store.commit("SET_USER_ROLE", role);
      if (role === "member") {
        this.$router.push("/member/home");
      } else if (role === "librarian") {
        this.$router.push("/librarian/home");
      }
    },
  },
};
</script>

<style scoped>
/* Your CSS here */
</style>

```

## SearchBar.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/SearchBar.vue`

```vue
<template>
  <div class="search-bar">
    <input type="text" v-model="searchQuery" @input="onSearch" placeholder="Search books" />
    <button @click="onSearch">
      <i class="fas fa-search"></i>
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    onSearch() {
      this.$emit('search', this.searchQuery);
    },
  },
};
</script>

<style scoped>
.search-bar {
  display: flex;
  align-items: center;
  padding: 10px;
}

.search-bar input {
  flex: 1;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.search-bar button {
  margin-left: 10px;
  padding: 8px 12px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>

```

## SideMenu.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/SideMenu.vue`

```vue
<template>
  <div class="side-menu" :class="{ open: isOpen }">
    <button
      class="toggle-button"
      @click="toggleMenu"
      aria-label="Toggle menu"
      aria-expanded="isOpen"
      aria-controls="side-menu-body"
    >
      <span class="line" :class="{ open: isOpen }"></span>
      <span class="line" :class="{ open: isOpen }"></span>
      <span class="line" :class="{ open: isOpen }"></span>
    </button>

    <transition name="slide">
      <div v-if="isOpen" id="side-menu-body" class="side-menu-body">
        <FilterSection
          v-for="filterType in filterTypes"
          :key="filterType"
          :title="filterType"
          :options="filters[filterType]"
          @filter-changed="onFilterChanged(filterType, $event)"
        />
      </div>
    </transition>
  </div>
</template>

<script>
import FilterSection from '@/components/FilterSection.vue';
import { genreService, authorService, bookService } from '@/services/ApiService';

export default {
  components: {
    FilterSection,
  },
  props: {
    isOpen: Boolean,
  },
  data() {
    return {
      filters: {},
      selectedFilters: {},
      isLoading: true,
      isError: false,
    };
  },
  async created() {
    try {
      const filters = await this.fetchFilters();
      this.filters = filters;
      this.selectedFilters = this.initializeSelectedFilters();
    } catch (error) {
      console.error(error);
      this.isError = true;
    } finally {
      this.isLoading = false;
    }
  },
  computed: {
    filterTypes() {
      return Object.keys(this.filters);
    },
  },
  methods: {
    async fetchFilters() {
      const [genres, authors, books] = await Promise.all([
        genreService.getAll(),
        authorService.getAll(),
        bookService.getAll(),
      ]);

      const distinctBookValues = new Map();
      books.forEach((book) => {
        for (const field of [
          'language',
          'type',
          'publisher',
          'publication_date',
          'free_access_in_memberships',
          'collections',
          'wishlists',
        ]) {
          const value = book[field];
          if (value !== null) {
            const set = distinctBookValues.get(field) || new Set();
            set.add(value);
            distinctBookValues.set(field, set);
          }
        }
      });

      return {
        genres,
        authors,
        languages: [...distinctBookValues.get('language')],
        ratings: [5, 4, 3, 2, 1],
        types: [...distinctBookValues.get('type')],
        publishers: [...distinctBookValues.get('publisher')],
        publicationDates: [...distinctBookValues.get('publication_date')],
        freeAccessInMemberships: [...distinctBookValues.get('free_access_in_memberships')],
        collections: [...distinctBookValues.get('collections')],
        wishlists: [...distinctBookValues.get('wishlists')],
      };
    },
    initializeSelectedFilters() {
      return Object.fromEntries(Object.keys(this.filters).map((key) => [key, []]));
    },
    onFilterChanged(filterType, selectedOptions) {
      this.selectedFilters[filterType] = selectedOptions;
      this.$emit('filter-changed', this.selectedFilters);
    },
    toggleMenu() {
      this.$emit('toggle');
    },
  },
};
</script>

<style scoped>
.side-menu {
  height: 100%;
}

.side-menu.open {
  width: 300px;
}

.toggle-button {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 30px;
  height: 24px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  z-index: 1;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.line {
  width: 100%;
  height: 3px;
  background-color: #333;
  transition: transform 0.3s, width 0.3s;
}

.line.open:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.line.open:nth-child(2) {
  transform: scaleX(0);
}

.line.open:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

.side-menu-body {
  padding: 10px;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}
</style>

```

## UserProfileEditComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/UserProfileEditComponent.vue`

```vue
<template>
    <div class="edit-profile">
      <h2>Edit Profile</h2>
      <form @submit.prevent="updateProfile">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="profile.username" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="profile.email" required>
        </div>
        <div>
          <label for="firstName">First Name:</label>
          <input type="text" id="firstName" v-model="profile.first_name">
        </div>
        <div>
          <label for="lastName">Last Name:</label>
          <input type="text" id="lastName" v-model="profile.last_name">
        </div>
        <button type="submit">Update Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  import { profileService } from '@/services/ApiService';
  
  export default {
    data() {
      return {
        profile: {},
      };
    },
    created() {
      this.fetchProfile();
    },
    methods: {
      async fetchProfile() {
        try {
          const userId = this.$store.getters.userId;
          this.profile = await profileService.getProfile(userId);
        } catch (error) {
          console.error('Error fetching profile:', error);
        }
      },
      async updateProfile() {
        try {
          await profileService.updateProfile(this.profile.id, this.profile);
          alert('Profile updated successfully');
          this.$router.push({ name: 'Profile' });
        } catch (error) {
          console.error('Error updating profile:', error);
        }
      },
    },
  };
  </script>

```

## UserProfileViewComponent.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/components/UserProfileViewComponent.vue`

```vue
<template>
    <div class="user-profile">
      <h2>User Profile</h2>
      <div>
        <label>Username:</label>
        <span>{{ profile.username }}</span>
      </div>
      <div>
        <label>Email:</label>
        <span>{{ profile.email }}</span>
      </div>
      <div>
        <label>First Name:</label>
        <span>{{ profile.first_name }}</span>
      </div>
      <div>
        <label>Last Name:</label>
        <span>{{ profile.last_name }}</span>
      </div>
      <button @click="editProfile">Edit Profile</button>
    </div>
  </template>
  
  <script>
  import { profileService } from '@/services/ApiService';
  
  export default {
    data() {
      return {
        profile: {},
      };
    },
    created() {
      this.fetchProfile();
    },
    methods: {
      async fetchProfile() {
        try {
          const userId = this.$store.getters.userId;
          this.profile = await profileService.getProfile(userId);
        } catch (error) {
          console.error('Error fetching profile:', error);
        }
      },
      editProfile() {
        this.$router.push({ name: 'EditProfile' });
      },
    },
  };
  </script>

```

## config.js
Path: `/home/milav/code/gppLMSv2/frontend/src/config.js`

```js
// config.js
const config = {
    development: {
      apiBaseUrl: "http://localhost:5000",
    },
    production: {
      apiBaseUrl: "https://api.example.com",
    },
  };
  
  export default config[process.env.NODE_ENV || "development"];

```

## main.js
Path: `/home/milav/code/gppLMSv2/frontend/src/main.js`

```js
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");

```

## index.js
Path: `/home/milav/code/gppLMSv2/frontend/src/router/index.js`

```js
import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MyLoansView from "@/views/MyLoansView.vue";
import LibrarianDashboardView from "@/views/LibrarianDashboardView.vue";
import MemberDashboardView from "@/views/MemberDashboardView.vue";
import BrowseLibraryView from '@/views/BrowseLibraryView.vue';

import UserProfileViewComponent from '@/components/UserProfileViewComponent.vue';
import UserProfileEditComponent from '@/components/UserProfileEditComponent.vue';

import UserRegistration from "@/components/auth/UserRegistration.vue";
import UserLogin from "@/components/auth/UserLogin.vue";
import UserLogout from "../components/auth/UserLogout.vue";
import ForgotPassword from "@/components/auth/ForgotPassword.vue";
import ChangePassword from "@/components/auth/ChangePassword.vue";

import RoleSelectionComponent from "@/components/RoleSelectionComponent.vue";
import BookLoanDetailsComponent from "@/components/BookLoanDetailsComponent.vue";

import BrowseBooks from "@/components/BrowseBooks.vue";
import BrowseGenres from "@/components/BrowseGenres.vue";
import GeneralList from "@/components/GeneralList.vue";
import GeneralEdit from "@/components/GeneralEdit.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/select-role",
    name: "SelectRole",
    component: RoleSelectionComponent,
  },

  {
    path: "/member/loans",
    name: "MyLoansView",
    component: MyLoansView,
  },

  {
    path: "/librarian/home",
    name: "LibrarianDashboardView",
    component: LibrarianDashboardView,
  },

  {
    path: "/member/home",
    name: "MemberDashboardView",
    component: MemberDashboardView,
  },
  {
    path: "/loan-details/:id",
    name: "LoanDetails",
    component: BookLoanDetailsComponent,
  },

  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },

  {
    path: '/member/profile',
    name: 'Profile',
    component: UserProfileViewComponent,
  },

  {
    path: '/member/profile/edit',
    name: 'EditProfile',
    component: UserProfileEditComponent,
  },

  {
    path: '/member/library',
    name: 'BrowseLibrary',
    component: BrowseLibraryView,
  },

  {
    path: "/login",
    name: "UserLogin",
    component: UserLogin,
  },
  {
    path: "/logout",
    name: "Logout",
    component: UserLogout,
  },
  {
    path: "/register",
    name: "UserRegister",
    component: UserRegistration,
  },
  {
    path: "/reset",
    name: "ForgotPassword",
    component: ForgotPassword,
  },
  {
    path: "/change",
    name: "ChangePassword",
    component: ChangePassword,
  },
  {
    path: "/browse-books",
    name: "BrowseBooks",
    component: BrowseBooks,
  },
  {
    path: "/browse-genres",
    name: "BrowseGenres",
    component: BrowseGenres,
  },

  {
    path: "/books/edit/:id",
    name: "EditBook",
    component: GeneralEdit,
    props: (route) => ({ type: "Book", id: route.params.id }),
  },

  {
    path: "/genres/edit/:id",
    name: "EditGenre",
    component: GeneralEdit,
    props: (route) => ({ type: "Genre", id: route.params.id }),
  },

  {
    path: "/authors/edit/:id",
    name: "EditAuthor",
    component: GeneralEdit,
    props: (route) => ({ type: "Author", id: route.params.id }),
  },

  {
    path: "/users/edit/:id",
    name: "EditUser",
    component: GeneralEdit,
    props: (route) => ({ type: "User", id: route.params.id }),
  },

  {
    path: "/books",
    component: GeneralList,
    props: {
      resourceType: "books",
      editRoute: "EditBook",
    },
  },

  {
    path: "/authors",
    component: GeneralList,
    props: {
      resourceType: "authors",
      editRoute: "EditAuthor",
    },
  },

  {
    path: "/genres",
    component: GeneralList,
    props: {
      resourceType: "genres",
      editRoute: "EditGenre",
    },
  },

  {
    path: "/users",
    component: GeneralList,
    props: {
      resourceType: "users",
      editRoute: "EditUser",
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;

```

## ApiService.js
Path: `/home/milav/code/gppLMSv2/frontend/src/services/ApiService.js`

```js
import axios from "axios";
import config from "@/config";

class ApiService {
  constructor(endpoint) {
    this.apiUrl = `${config.apiBaseUrl}/${endpoint}`;
  }

  async create(data) {
    const response = await axios.post(this.apiUrl, data);
    return response.data;
  }

  async getAll(filters = {}, sort_by = {}, sort_order = {}) {
    const queryParams = {
      filters: filters,
      sort_by: sort_by,
      sort_order: sort_order,
    };
    const response = await axios.get(this.apiUrl, { params: queryParams });
    return response.data;
  }

  async getById(id) {
    const response = await axios.get(`${this.apiUrl}/${id}`);
    return response.data;
  }

  async update(id, data) {
    const response = await axios.put(`${this.apiUrl}/${id}`, data);
    return response.data;
  }

  async delete(id) {
    const response = await axios.delete(`${this.apiUrl}/${id}`);
    return response.data;
  }
}

class BookLoanService extends ApiService {
  async fetchLoans(filter) {
    const loanData = await this.getAll(filter);
    return Promise.all(
      loanData.map(async (loan) => {
        const book = await bookService.getById(loan.book_id);
        loan.bookTitle = book.title;
        return loan;
      })
    );
  }

  async requestLoan(bookId, memberId) {
    const loan = {
      book_id: bookId,
      member_id: memberId,
      status: "requested",
    };
    return this.create(loan);
  }

  async approveLoan(id) {
    const response = await axios.put(`${this.apiUrl}/${id}/approve`);
    return response.data;
  }

  async returnLoan(loanId) {
    const loan = await this.getById(loanId);
    if (loan.status === "approved") {
      const updatedLoanData = {
        book_id: loan.book_id,
        member_id: loan.member_id,
        status: "returned",
        returned_date: new Date().toISOString().split("T")[0],
      };
      await this.update(loanId, updatedLoanData);
    }
  }
}

class ProfileService extends ApiService {
  async getProfile(userId) {
    const response = await axios.get(`${this.apiUrl}/${userId}`);
    return response.data;
  }

  async updateProfile(userId, data) {
    const response = await axios.put(`${this.apiUrl}/${userId}`, data);
    return response.data;
  }
}

class BookService extends ApiService {
  async getByGenre(genreId) {
    const response = await axios.get(`${this.apiUrl}`, {
      params: {
        "filters[genres][id]": genreId,
      },
    });
    return response.data;
  }
}

export default ApiService;

export const userService = new ApiService("api/users");
export const authorService = new ApiService("api/authors");
export const genreService = new ApiService("api/genres");
export const bookService = new BookService("api/books");
export const bookLoanService = new BookLoanService("api/bookloans");
export const profileService = new ProfileService("api/profile");

```

## store.js
Path: `/home/milav/code/gppLMSv2/frontend/src/store.js`

```js
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
import config from "@/config";

Vue.use(Vuex);

const apiBaseUrl = config.apiBaseUrl;

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: ["user"],
    }),
  ],

  state: {
    user: null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_USER_ROLE(state, role) {
      if (state.user) {
        state.user.role = role;
      }
    },
    CLEAR_USER(state) {
      state.user = null;
    },
    CLEAR_USER_ROLE(state, role) {
      if (state.user) {
        state.user.role = role;
      }
    },
  },
  actions: {
    async register({ dispatch }, credentials) {
      try {
        const response = await axios.post(
          `${apiBaseUrl}/register`,
          credentials,
          {
            params: {
              include_auth_token: true,
            },
          }
        );
        localStorage.setItem(
          "authToken",
          response.data.response.user.authentication_token
        );
        axios.defaults.headers.common["Authentication-Token"] =
          localStorage.authToken;
        await dispatch("fetchUser");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async login({ dispatch }, credentials) {
      try {
        const response = await axios.post(
          `${apiBaseUrl}/login`,
          credentials,
          {
            params: {
              include_auth_token: true,
            },
          }
        );
        localStorage.setItem(
          "authToken",
          response.data.response.user.authentication_token
        );
        axios.defaults.headers.common["Authentication-Token"] =
          localStorage.authToken;
        await dispatch("fetchUser");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async fetchUser({ commit }) {
      const token = localStorage.getItem("authToken");
      if (token) {
        try {
          const userResponse = await axios.get(
            `${apiBaseUrl}/api/current_user`
          );
          commit("SET_USER", userResponse.data);
        } catch (error) {
          console.error("Error fetching user:", error);
        }
      }
    },

    async logout({ commit }) {
      try {
        await axios.post(`${apiBaseUrl}/logout`);
        localStorage.removeItem("authToken");
        axios.defaults.headers.common["Authentication-Token"] = "";
        commit("CLEAR_USER");
        commit("CLEAR_USER_ROLE");
      } catch (error) {
        console.error("Logout failed:", error);
      }
    },
  },

  getters: {
    userId(state) {
      return state.user.id;
    },
  },
});

```

## filterBooks.js
Path: `/home/milav/code/gppLMSv2/frontend/src/utils/filterBooks.js`

```js
// src/utils/filterBooks.js
export default function filterBooks(books, searchQuery, selectedFilters) {
    return books.filter((book) => {
      const matchesQuery = !searchQuery || book.title.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesFilters = Object.keys(selectedFilters).every((filterType) => {
        const filterOptions = selectedFilters[filterType];
        if (filterOptions.length === 0) return true;
        if (filterType === 'genres') {
          return book.genres.some((genre) => filterOptions.includes(genre.id));
        } else if (filterType === 'authors') {
          return book.authors.some((author) => filterOptions.includes(author.id));
        } else if (filterType === 'freeAccessInMemberships') {
          return book.free_access_in_memberships.some((membership) => filterOptions.includes(membership.id));
        } else if (filterType === 'collections') {
          return book.collections.some((collection) => filterOptions.includes(collection.id));
        } else if (filterType === 'wishlists') {
          return book.wishlists.some((wishlist) => filterOptions.includes(wishlist.id));
        } else {
          return filterOptions.includes(book[filterType]);
        }
      });
      return matchesQuery && matchesFilters;
    });
  }

```

## AboutView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/AboutView.vue`

```vue
<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

```

## BrowseLibraryView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/BrowseLibraryView.vue`

```vue
<!-- src/views/BrowseLibraryView.vue -->
<template>
  <div class="browse-library">
    <BrowseGenre @genre-selected="onGenreSelected" />
    <div class="books-container">
      <BrowseBooks @loan-created="onLoanCreated" ref="browseBooks" />
    </div>
  </div>
</template>

<script>
import BrowseGenre from '@/components/BookBrowsing/BrowseGenre.vue';
import BrowseBooks from '@/components/BookBrowsing/BrowseBooks.vue';

export default {
  components: {
    BrowseGenre,
    BrowseBooks,
  },
  methods: {
    onGenreSelected(genre) {
      this.$refs.browseBooks.selectedFilters.genres = [genre.id];
    },
    onLoanCreated() {
      // Handle loan creation, e.g., show a success message
    },
  },
};
</script>

<style scoped>
.browse-library {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.main-content {
  display: flex;
  flex: 1;
}
</style>

```

## HomeView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/HomeView.vue`

```vue
<template>
  <div>
    <browse-books> </browse-books>
    <browse-genres> </browse-genres>
  </div>
</template>

<script>
import BrowseBooks from "@/components/BrowseBooks.vue";
import BrowseGenres from "@/components/BrowseGenres.vue";

export default {
  components: {
    BrowseBooks,
    BrowseGenres,
  },
};
</script>

```

## LibrarianDashboardView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/LibrarianDashboardView.vue`

```vue
<template>
  <div>
    <h1>Welcome Librarian</h1>
    <ul>
      <li>
        <router-link to="/users">User Management</router-link>
      </li>
      <li>
        <router-link to="/books">Book Management</router-link>
      </li>
      <li>
        <router-link to="/genres">Genre Management</router-link>
      </li>
      <li>
        <router-link to="/authors">Author Management</router-link>
      </li>
    </ul>
    <book-loan-requests-list-component />
    <book-loans-list-component />
  </div>
</template>

<script>
import BookLoanRequestsListComponent from '@/components/BookLoanRequestsListComponent';
import BookLoansListComponent from '@/components/BookLoansListComponent';

export default {
  components: {
    BookLoanRequestsListComponent,
    BookLoansListComponent
  }
};
</script>

```

## MemberDashboardView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/MemberDashboardView.vue`

```vue
<template>
  <div>
    <h1>Welcome Member</h1>
    <ul>
      <li>
        <router-link to="/member/loans">Member Loans</router-link>
      </li>
      <li>
        <router-link to="/member/profile">Member Profile</router-link>
      </li>
      <li>
        <router-link to="/browse-books">Browse Books</router-link>
      </li>
      <li>
        <router-link to="/browse-genres">Browse Genres</router-link>
      </li>
      <li>
        <router-link to="/member/library">Browse Library</router-link>
      </li>
    </ul>
    <book-loan-request-component />
    <book-loans-list-component />
  </div>
</template>

<script>
import BookLoanRequestComponent from '@/components/BookLoanRequestComponent';
import BookLoansListComponent from '@/components/BookLoansListComponent';

export default {
  components: {
    BookLoanRequestComponent,
    BookLoansListComponent
  }
};
</script>

```

## MyLoansView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/MyLoansView.vue`

```vue
<template>
  <div>
    <!-- Display user's loans -->
    <book-loans-list-component />
  </div>
</template>

<script>
import BookLoansListComponent from '@/components/BookLoansListComponent';

export default {
  components: {
    BookLoansListComponent
  }
};
</script>

```

## ProfileView.vue
Path: `/home/milav/code/gppLMSv2/frontend/src/views/ProfileView.vue`

```vue
<template>
    <div class="profile">
        <h2>User Profile</h2>
        <form @submit.prevent="updateProfile">
            <div>
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="profile.username" required>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" v-model="profile.email" required>
            </div>
            <div>
                <label for="firstName">First Name:</label>
                <input type="text" id="firstName" v-model="profile.first_name">
            </div>
            <div>
                <label for="lastName">Last Name:</label>
                <input type="text" id="lastName" v-model="profile.last_name">
            </div>
            <button type="submit">Update Profile</button>
        </form>
    </div>
</template>

<script>
import { profileService } from '@/services/ApiService';

export default {
    data() {
        return {
            profile: {},
        };
    },
    created() {
        this.fetchProfile();
    },
    methods: {
        async fetchProfile() {
            try {
                const userId = this.$store.getters.userId;
                this.profile = await profileService.getProfile(userId);
            } catch (error) {
                console.error('Error fetching profile:', error);
            }
        },
        async updateProfile() {
            try {
                await profileService.updateProfile(this.profile.id, this.profile);
                alert('Profile updated successfully');
            } catch (error) {
                console.error('Error updating profile:', error);
            }
        },
    },
};
</script>

```

## vue.config.js
Path: `/home/milav/code/gppLMSv2/frontend/vue.config.js`

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

```

