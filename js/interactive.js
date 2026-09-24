// Scroll Progress Bar
(function () {
  var progressContainer = document.createElement('div');
  progressContainer.className = 'progress-container';
  var progressBar = document.createElement('div');
  progressBar.className = 'progress-bar';
  progressBar.id = 'myBar';
  progressContainer.appendChild(progressBar);
  
  if (document.body && !document.getElementById('myBar')) {
    document.body.insertBefore(progressContainer, document.body.firstChild);
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      if (!document.getElementById('myBar')) {
        document.body.insertBefore(progressContainer, document.body.firstChild);
      }
    });
  }

  window.addEventListener('scroll', function () {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = height ? (winScroll / height) * 100 : 0;
    var bar = document.getElementById('myBar');
    if (bar) bar.style.width = scrolled + '%';
  });
})();

// 3D Parallax Card Tilt (desktop / pointer devices only)
(function () {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (window.location.href.indexOf('uxwriting') !== -1) return;
  document.querySelectorAll('.sample-card').forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      var rect = card.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      var centerX = rect.width / 2;
      var centerY = rect.height / 2;
      var rotateX = ((y - centerY) / centerY) * -5;
      var rotateY = ((x - centerX) / centerX) * 5;
      card.style.transform = 'perspective(1000px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) scale3d(1.02, 1.02, 1.02)';
    });
    card.addEventListener('mouseleave', function () {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      card.style.transition = 'transform 0.5s ease-out';
    });
    card.addEventListener('mouseenter', function () {
      card.style.transition = 'none';
    });
  });
})();

// Constellation Particles (Subtle Atmospheric Background - Non-Distracting)
(function () {
  var sections = document.querySelectorAll('.hero-section, .bg-custom-dark:not(.navbar)');
  sections.forEach(function (section) {
    if (!section.querySelector('.particles-canvas')) {
      var canvas = document.createElement('canvas');
      canvas.className = 'particles-canvas';
      canvas.setAttribute('aria-hidden', 'true');
      section.insertBefore(canvas, section.firstChild);
    }
  });

  var canvases = document.querySelectorAll('.particles-canvas');
  canvases.forEach(function(canvas) {
    if (!canvas || !canvas.getContext) return;
    var ctx = canvas.getContext('2d');
    var particles = [];
    // Balanced, polite star count
    var count = window.innerWidth < 768 ? 30 : 65;

    function resize() {
      canvas.width = canvas.parentElement.offsetWidth;
      canvas.height = canvas.parentElement.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    function Particle() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.vx = (Math.random() - 0.5) * 0.22; // Calm, slow drift
      this.vy = (Math.random() - 0.5) * 0.22;
      this.r = Math.random() * 0.9 + 0.5; // Delicate pinpricks (0.5px to 1.4px)
      this.o = Math.random() * 0.22 + 0.12; // Muted, comfortable starlight
    }
    Particle.prototype.update = function () {
      this.x += this.vx;
      this.y += this.vy;
      if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
      if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
    };
    Particle.prototype.draw = function () {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(212,209,206,' + this.o + ')';
      ctx.fill();
    };

    for (var p = 0; p < count; p++) particles.push(new Particle());

    // Delicate Aries Constellation (Soft subtle accent)
    var aries = {
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.25,
      vy: (Math.random() - 0.5) * 0.25,
      angle: Math.random() * Math.PI * 2,
      vAngle: (Math.random() - 0.5) * 0.003,
      nodes: [
        { dx: -35, dy: 12, size: 1.5 },
        { dx: 0, dy: 0, size: 2.0 },
        { dx: 24, dy: -16, size: 1.8 },
        { dx: 48, dy: -4, size: 1.4 }
      ],
      update: function() {
        this.x += this.vx;
        this.y += this.vy;
        this.angle += this.vAngle;
        if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
        if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
      },
      draw: function() {
        var pts = [];
        var cos = Math.cos(this.angle);
        var sin = Math.sin(this.angle);
        for(var i=0; i<this.nodes.length; i++) {
          var n = this.nodes[i];
          var nx = this.x + n.dx * cos - n.dy * sin;
          var ny = this.y + n.dx * sin + n.dy * cos;
          pts.push({x: nx, y: ny, size: n.size});
        }
        
        // Whispering golden lines
        ctx.beginPath();
        ctx.moveTo(pts[0].x, pts[0].y);
        ctx.lineTo(pts[1].x, pts[1].y);
        ctx.lineTo(pts[2].x, pts[2].y);
        ctx.lineTo(pts[3].x, pts[3].y);
        ctx.strokeStyle = 'rgba(232, 196, 124, 0.20)';
        ctx.lineWidth = 0.8;
        ctx.stroke();

        // Subtle stars
        for(var i=0; i<pts.length; i++) {
          ctx.beginPath();
          ctx.arc(pts[i].x, pts[i].y, pts[i].size, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(255, 255, 255, 0.65)';
          ctx.fill();
        }
      }
    };

    var mouseX = -9999, mouseY = -9999;
    var parentEl = canvas.parentElement;
    parentEl.addEventListener('mousemove', function (e) {
      var rect = parentEl.getBoundingClientRect();
      mouseX = e.clientX - rect.left;
      mouseY = e.clientY - rect.top;
    });
    parentEl.addEventListener('mouseleave', function () {
      mouseX = -9999;
      mouseY = -9999;
    });

    function frame() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      for (var i = 0; i < particles.length; i++) {
        var dx0 = particles[i].x - mouseX;
        var dy0 = particles[i].y - mouseY;
        var dist0 = Math.sqrt(dx0 * dx0 + dy0 * dy0);
        if (dist0 < 90 && dist0 > 0) {
          particles[i].x += (dx0 / dist0) * 0.3; // Gentle non-jarring deflection
          particles[i].y += (dy0 / dist0) * 0.3;
        }
        particles[i].update();
        particles[i].draw();
        for (var j = i + 1; j < particles.length; j++) {
          var dx = particles[i].x - particles[j].x;
          var dy = particles[i].y - particles[j].y;
          var d = Math.sqrt(dx * dx + dy * dy);
          if (d < 110) {
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            // Whisper-soft lines: elegant atmospheric depth without competing with text
            ctx.strokeStyle = 'rgba(212,209,206,' + (0.10 * (1 - d / 110)) + ')';
            ctx.lineWidth = 0.6;
            ctx.stroke();
          }
        }
      }
      
      aries.update();
      aries.draw();

      requestAnimationFrame(frame);
    }
    frame();
  });
})();
// Carousel Touch Swipe Support
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var carousels = document.querySelectorAll('.carousel');
    carousels.forEach(function(carousel) {
      var touchStartX = 0;
      var touchEndX = 0;
      
      carousel.addEventListener('touchstart', function(event) {
        touchStartX = event.changedTouches[0].screenX;
      }, {passive: true});
      
      carousel.addEventListener('touchend', function(event) {
        touchEndX = event.changedTouches[0].screenX;
        handleSwipe();
      }, {passive: true});
      
      function handleSwipe() {
        var swipeThreshold = 40; // minimum distance to trigger swipe
        if (touchEndX < touchStartX - swipeThreshold) {
          // swipe left -> next
          var nextBtn = carousel.querySelector('.carousel-control-next');
          if (nextBtn) nextBtn.click();
        }
        if (touchEndX > touchStartX + swipeThreshold) {
          // swipe right -> prev
          var prevBtn = carousel.querySelector('.carousel-control-prev');
          if (prevBtn) prevBtn.click();
        }
      }
    });
  });
})();
