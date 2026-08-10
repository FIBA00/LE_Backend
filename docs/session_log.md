# TLang Development Session Log

This file tracks the progress, decisions, and immediate TODOs for each development session.

## 📝 Current Session Notes

- **July 8, 2025:**
  - Reviewed existing UI components (`App.jsx`, `EditorWidget.jsx`, `NoteWidget.jsx`).
  - Confirmed `react-grid-layout` and Monaco Editor are integrated.
  - Established `session_log.md` as the primary file for tracking session progress and TODOs, leaving `project_guide.md` as a static project specification.
  - Integrated `MarkdownEditor` component into `NoteWidget.jsx` for enhanced note-taking capabilities.
  - Implemented a toggle button in `NoteWidget.jsx` to hide/show the markdown preview.
  - Updated `frontend/index.html` with a dark background and a 3D deep space effect.
  - Modified `App.jsx` to expose the `react-grid-layout` grid and apply a background style.
  - Styled `NoteWidget.jsx` and `EditorWidget.jsx` with semi-transparent backgrounds and subtle borders to complement the new background.
  - **Major Architectural Shift:** Decided to move from `react-grid-layout` to `reactflow` for an infinite, zoomable canvas.
  - Installed `reactflow` library.
  - Created `frontend/src/components/Canvas.jsx` to house the React Flow canvas, including drag-and-drop functionality and custom node types.
  - Created `frontend/src/components/ToolPalette.jsx` for draggable tools.
  - Updated `App.jsx` to use the new `Canvas` and `ToolPalette` components.
  - Adapted `NoteWidget.jsx` and `EditorWidget.jsx` to function as React Flow custom nodes, accepting `data` props.
  - Created `frontend/src/components/TopBar.jsx` for global actions.
  - Implemented zoom in/out functionality via `TopBar` and `Canvas`.
  - Implemented dynamic background warping effect based on canvas drag/pan.
  - Removed zoom buttons from `TopBar.jsx`.
  - Created `frontend/src/components/WidgetWrapper.jsx` to standardize widget appearance and provide resizing.
  - Wrapped `NoteWidget.jsx` and `EditorWidget.jsx` with `WidgetWrapper`.
  - Updated `Canvas.jsx` to set standard sizes for new nodes.
  - Modified `ToolPalette.jsx` to use icon-based tools with hover-to-expand functionality.
  - Implemented minimize and destroy functionality for widgets via `WidgetWrapper` and `Canvas.jsx`.
  - **Backend for Notes:** Created `backend/routes/notes.py` with save/load endpoints and integrated it into `app.py`. Added `/list` endpoint to list all saved notes.
  - **Frontend for Notes:** Added Save/Load buttons to `NoteWidget.jsx` and connected them to the Flask API. Added a dropdown to load existing notes.
  - **Backend for Code Files:** Created `backend/routes/code.py` with list, load, and save endpoints and integrated it into `app.py`.
  - **Frontend for Code Files:** Added file management UI (save, load, new file, file list) to `EditorWidget.jsx` and connected it to the Flask API.
  - **Debugging:** Addressed unresponsive loop and editor issues by simplifying `onMinimize` logic in `Canvas.jsx` and ensuring robust default values for widget props.
  - **Fixes:** Added `id` to `MarkdownEditor` textarea. Implemented z-index management in `Canvas.jsx` for selected nodes. Memoized `customNodeTypes` in `Canvas.jsx` to resolve React Flow warning. Fixed duplicate ID generation in `Canvas.jsx` using `crypto.randomUUID()`. Corrected `onMinimize` logic in `Canvas.jsx` to explicitly update node height and manage position for minimized state. Added `e.stopPropagation()` to minimize/destroy buttons in `WidgetWrapper.jsx` to prevent unintended resizing. Configured `reactflow` to use a specific drag handle (`.draghandle`) in `WidgetWrapper.jsx` to allow interaction with internal elements of the widgets. Removed `nodrag` class from `WidgetWrapper`'s root div to enable resizing. Modified `MinimizedWidgetsBar.jsx` to display widgets horizontally and as icons. Added temporary red border to `NodeResizer` in `WidgetWrapper.jsx` for debugging resizing issues. Configured `reactflow` to use a specific drag handle (`.draghandle`) in `WidgetWrapper.jsx` to allow interaction with internal elements of the widgets. Added `e.stopPropagation()` to minimize/destroy buttons in `WidgetWrapper.jsx` to prevent unintended resizing.
  - **New Feature:** Implemented `MinimizedWidgetsBar.jsx` to display minimized widgets and added unminimize functionality.
  - **Temporary Change:** Replaced Monaco Editor with a simple `textarea` in `EditorWidget.jsx` for easier testing and development.
  - **Backend for Code Files:** Created `backend/routes/code.py` with list, load, and save endpoints and integrated it into `app.py`.

## ✅ TODO

- **UI Refinement:**
  - Improve styling and layout of existing widgets (`NoteWidget`, `EditorWidget`).
  - Implement responsive design for various screen sizes.
  - Integrate a consistent theme (e.g., dark mode, neon borders as per "space aesthetic").
- **Tool Spawner Module:**
  - Implement basic `ToolSpawner` functionality (e.g., embedding iframes for YouTube, Code-server).
  - Add UI elements to spawn and manage tools.
- **Backend Integration:**
  - Connect `NoteWidget` to Flask backend for saving/loading notes.
  - Connect `EditorWidget` to backend for syntax comparison/translation (if not already done).
- **New Features (from Key Features section in project_guide.md):**
  - MFP (Micro Fluency Practice) module.
  - Progress Tracker.
  - Account System (optional).
