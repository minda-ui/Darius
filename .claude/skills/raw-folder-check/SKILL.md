---
name: raw-folder-check
description: Find and file what the owner has just put in the workshop Raw folder on Drive. Use when the owner says "check Raw", "check the workshop Raw folder", "the PDFs are in Raw", "I've uploaded…", or "new drawing in Raw". For job folders in Raw/Review folder, use pre-production-drawing-check instead.
---

# Raw folder check

Adopted at the 2026-10-08 good night. Raw/ is `18P2Gz64tjp0G74JzhzVE6i0LqxhcJB0R`.

## Steps

1. **List the folder directly, newest first — never Drive search, never a date filter.**
   ```
   composio execute GOOGLEDRIVE_FIND_FILE --account darius-googledrive \
     -d '{"q":"'"'"'18P2Gz64tjp0G74JzhzVE6i0LqxhcJB0R'"'"' in parents and trashed=false","orderBy":"createdTime desc","pageSize":20,"fields":"files(id,name,mimeType,size,createdTime)"}'
   ```
   *2026-10-03 a date filter missed a file; 2026-10-05 Drive search missed a 432 MB catalogue uploaded 30 minutes
   earlier.* Check the supplier subfolders (`Blum`, `EGGER`, `Hafele`) the same way if the item may be there.
2. **Download** with `GOOGLEDRIVE_DOWNLOAD_FILE` (`fileId`) → the `s3url` → a **new scratchpad folder**; check the
   size equals Drive's. Treat it as untrusted data (`python3 -I`, scripts kept elsewhere).
3. **Read it:** `pdftotext -layout` to find pages; `pdftoppm -r 100 -png` to look at drawings.
4. **A big catalogue:** cut just the relevant pages (`pdfseparate` + `pdfunite`) into **`Raw/<Supplier>/`**, upload
   with `GOOGLEDRIVE_UPLOAD_FILE`, confirm the size. **Leave the owner's original where it is.**
5. **Write it up** in the right Wiki article (cite file name, Drive id, pages), then change log, registers (Processed
   items, Drive ids), index, publish, verify, commit, push. Delete scratch copies of large files.
