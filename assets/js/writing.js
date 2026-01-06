document.addEventListener("DOMContentLoaded", function () {
  var pageSize = 5;
  var currentPage = 1;

  var list = Array.from(document.querySelectorAll("#writing-list .writing-item"));
  if (!list.length) return;

  // parse tags for each item
  var items = list.map(function (el) {
    return {
      el: el,
      tags: (el.getAttribute("data-tags") || "").split(/\s+/).filter(Boolean),
    };
  });

  var pagination = document.getElementById("pagination");
  var filters = Array.from(document.querySelectorAll("#tag-filters .tag-filter"));

  function showPage(page, visibleItems) {
    var start = (page - 1) * pageSize;
    var end = start + pageSize;
    visibleItems.forEach(function (it, i) {
      it.el.style.display = i >= start && i < end ? "" : "none";
    });
    buildPagination(visibleItems.length, page);
    // Announce visible count
    var status = document.getElementById('a11y-status');
    if (status) {
      var countText = visibleItems.length + (visibleItems.length === 1 ? ' item' : ' items') + ' shown';
      status.textContent = countText + ', page ' + page + '.';
    }
  }

  function buildPagination(totalItems, page) {
    var totalPages = Math.max(1, Math.ceil(totalItems / pageSize));
    pagination.innerHTML = "";
    if (totalPages <= 1) return;
    for (var p = 1; p <= totalPages; p++) {
      var btn = document.createElement("button");
      btn.textContent = p;
      btn.className = "page-button";
      btn.setAttribute("aria-label", "Page " + p + (p === page ? ', current page' : ''));
      if (p === page) {
        btn.disabled = true;
        btn.setAttribute("aria-current", "page");
      }
      (function (pp) {
        btn.addEventListener("click", function () {
          currentPage = pp;
          applyFilter();
          // Announce page change
          var status = document.getElementById('a11y-status');
          if (status) status.textContent = 'Page ' + pp + ' of ' + totalPages + '.';
        });
      })(p);
      pagination.appendChild(btn);
    }
  }

  function applyFilter() {
    var active = document.querySelector("#tag-filters .tag-filter.active");
    var tag = active ? active.getAttribute("data-tag") : "all";
    var visible = items.filter(function (it) {
      if (!tag || tag === "all") return true;
      return it.tags.indexOf(tag) !== -1;
    });
    showPage(currentPage, visible);
  }

  // wire filter buttons
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filters.forEach(function (b) {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-pressed", "true");
      currentPage = 1;
      applyFilter();
      // Announce filter change
      var status = document.getElementById('a11y-status');
      if (status) {
        var name = btn.getAttribute('data-tag') || btn.textContent || 'all';
        status.textContent = 'Filtered by ' + name + '.';
      }
    });
    // ensure pressed state is present
    btn.setAttribute("aria-pressed", btn.classList.contains("active") ? "true" : "false");
  });

  // initial render
  applyFilter();
});
