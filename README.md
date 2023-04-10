CIF Print Server
------------------
Creation of a new print server for CIF that eliminates bloat and allows greater maintainability.

Start-Up
------------------
Pull the repository, and set up a virtual environment. Download the dependencies from requirements.txt, and serve the Flask App.

To-Do
------------------
Homepage
- [x] Fix side text alignment
- [ ] Link intro paragraph to CIF registration
- [ ] Add more content and details about CIF printing
- [ ] Format content within the grid layout

Print Pages
- [x] Fix side text alignment
- [x] Remove select page range and automatically display page range when print all pages is left unchecked
- [ ] Add drop box for file upload
- [ ] Add document display
- [ ] Add pop-ups for invalid form fill
- [ ] Create redirect page to send users to after printing
- [ ] Fix spacing with form fields
- [ ] Ensure page length fits within the document page length

About
- [ ] Find content for about page or remove altogether

General
- [ ] Swap database type to sqlite
- [ ] Add back in login functionality when complete