uv run nuitka `
    --standalone `
    --onefile `
    --enable-console `
    --windows-icon-from-ico="G:\1.WORK\CODEBASE\PY\CACHEPURGER\CachePurger\Assets\logo.ico" `
    --windows-uac-admin `
    main.py


# manual build
# uv run nuitka --standalone --onefile --enable-console --windows-icon-from-ico="G:\1.WORK\CODEBASE\PY\CACHEPURGER\CachePurger\Assets\logo.ico" --windows-uac-admin "G:\1.WORK\CODEBASE\PY\CACHEPURGER\CachePurger\main.py"