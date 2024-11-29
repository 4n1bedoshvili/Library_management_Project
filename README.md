A library management system built using Django and Django REST Framework. 
The system allows library employees to manage books, track book lending/return history, and users to register, browse books, and reserve them. 

**Project Features**
- **User Registration and Authentication**:
  - Users can register with required details.
  - Employees can be added via the admin panel.
  - Both users and employees can log in using authorization mechanisms.

- **Book Management**:
  - Employees can add, delete, and update books via the Django admin panel.
  - Books have detailed information such as title, authors, genre, publication date, and quantity in stock.
  - Authors and genres are separate models linked to books with appropriate relationships.

- **Book Lending and Reservations**:
  - Users can view the book list with filtering, search, and pagination.
  - Users can reserve books for one day. If not checked out within this time, the reservation is automatically canceled via a management command.
  - Librarians can track the borrowing and returning of books.

- **Statistics API**:
  - Provides the 10 most popular books based on borrowing data.
  - Shows how many times each book was checked out in the last year.
 
    **Technologies Used**
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (default, configurable)
- **Authentication**: Django’s built-in authentication system
- **API Pagination**: DRF Pagination
- **Scheduled Tasks**: Management commands for reservation auto-cancelation
