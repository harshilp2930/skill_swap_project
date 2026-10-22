document.addEventListener('DOMContentLoaded', function() {
    // --- Smooth Page Transitions for Internal Links ---
    document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (!link) return;

        const href = link.getAttribute('href');
        if (!href) return;

        // Skip non-navigational or special links
        if (
            link.target === '_blank' ||
            link.hasAttribute('download') ||
            e.ctrlKey || e.metaKey || e.shiftKey || e.altKey ||
            e.defaultPrevented ||
            href.startsWith('#') ||
            href.startsWith('javascript:') ||
            href.startsWith('mailto:') ||
            href.startsWith('tel:')
        ) {
            return;
        }

        try {
            const targetUrl = new URL(link.href, window.location.origin);
            if (targetUrl.origin !== window.location.origin) return; // External link

            // Skip if same page
            if (targetUrl.pathname === window.location.pathname && targetUrl.search === window.location.search) {
                return;
            }

            e.preventDefault();
            document.body.classList.remove('page-loaded');
            document.body.classList.add('page-leaving');

            setTimeout(() => {
                window.location.href = link.href;
            }, 120);
        } catch (err) {
            // Default link action if URL parsing fails
        }
    });

    // Handle bfcache or back/forward navigation
    window.addEventListener('pageshow', function() {
        document.body.classList.remove('page-leaving');
        document.body.classList.add('page-loaded');
    });

    // Ensure body is loaded
    document.body.classList.add('page-loaded');

    // --- Sidebar Handling ---
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    const desktopToggleButton = document.getElementById('desktop-sidebar-toggle');
    const mobileMenuButton = document.getElementById('mobile-menu-button');

    const setInitialSidebarState = () => {
        const isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
        if (window.innerWidth >= 768 && isCollapsed) {
            sidebar.classList.add('sidebar-collapsed');
            if (mainContent) mainContent.classList.add('main-content-shifted');
        }
        requestAnimationFrame(() => {
            sidebar.classList.add('sidebar-ready');
        });
    };

    const toggleSidebar = () => {
        if (!sidebar.classList.contains('sidebar-ready')) return;
        sidebar.classList.toggle('sidebar-collapsed');
        if (mainContent) mainContent.classList.toggle('main-content-shifted');

        if (window.innerWidth >= 768) {
            const isCollapsed = sidebar.classList.contains('sidebar-collapsed');
            localStorage.setItem('sidebarCollapsed', isCollapsed);
        }
    };

    if (sidebar && desktopToggleButton) {
        setInitialSidebarState();
        desktopToggleButton.addEventListener('click', toggleSidebar);
    }

    if (mobileMenuButton && sidebar) {
        mobileMenuButton.addEventListener('click', () => {
            sidebar.classList.toggle('sidebar-closed');
        });
    }

    // --- Smooth Modal Helpers ---
    window.openModalWithAnimation = function(modalEl) {
        if (!modalEl) return;
        modalEl.classList.remove('hidden');
        modalEl.style.display = 'flex';
        requestAnimationFrame(() => {
            modalEl.classList.add('is-open');
        });
        document.body.style.overflow = 'hidden';
    };

    window.closeModalWithAnimation = function(modalEl) {
        if (!modalEl) return;
        modalEl.classList.remove('is-open');
        setTimeout(() => {
            modalEl.classList.add('hidden');
            modalEl.style.display = '';
            document.body.style.overflow = '';
        }, 200);
    };

    // --- Contact User Modal Logic ---
    const contactModal = document.getElementById('contact-modal');
    if (contactModal) {
        const closeModalButton = document.getElementById('close-modal');
        const closeModalBtn = document.getElementById('close-modal-btn');
        const contactButtons = document.querySelectorAll('.contact-btn');
        const modalUsername = document.getElementById('modal-username');
        const modalEmail = document.getElementById('modal-email');

        const openContactModal = (username, email) => {
            if (modalUsername) modalUsername.textContent = username;
            if (modalEmail) modalEmail.textContent = email;
            window.openModalWithAnimation(contactModal);
        };

        const closeContactModal = () => {
            window.closeModalWithAnimation(contactModal);
        };

        contactButtons.forEach(button => {
            button.addEventListener('click', () => {
                const username = button.dataset.username || button.getAttribute('data-username');
                const email = button.dataset.email || button.getAttribute('data-email');
                openContactModal(username, email);
            });
        });

        closeModalButton?.addEventListener('click', closeContactModal);
        closeModalBtn?.addEventListener('click', closeContactModal);

        contactModal.addEventListener('click', (e) => {
            if (e.target === contactModal || e.target.classList.contains('modal-backdrop')) {
                closeContactModal();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !contactModal.classList.contains('hidden')) {
                closeContactModal();
            }
        });
    }

    // --- Delete Confirmation Modal Logic ---
    const deleteModal = document.getElementById('delete-modal');
    if (deleteModal) {
        const cancelDeleteButton = document.getElementById('cancel-delete');
        const deleteForm = document.getElementById('delete-form');
        const deleteButtons = document.querySelectorAll('.delete-btn');

        const openDeleteModal = (deleteUrl) => {
            if (deleteForm) deleteForm.action = deleteUrl;
            window.openModalWithAnimation(deleteModal);
        };

        const closeDeleteModal = () => {
            window.closeModalWithAnimation(deleteModal);
        };

        deleteButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                e.preventDefault();
                const deleteUrl = button.dataset.url || button.getAttribute('data-url');
                openDeleteModal(deleteUrl);
            });
        });

        cancelDeleteButton?.addEventListener('click', closeDeleteModal);

        deleteModal.addEventListener('click', (e) => {
            if (e.target === deleteModal || e.target.classList.contains('modal-backdrop')) {
                closeDeleteModal();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !deleteModal.classList.contains('hidden')) {
                closeDeleteModal();
            }
        });
    }
});
