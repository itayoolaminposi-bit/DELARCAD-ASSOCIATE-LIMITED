GET_STARTED_BODY = """
<section class="page-hero">
  <div class="wrap">
    <span class="mono-label">GET STARTED</span>
    <h1>Tell us about your project</h1>
    <p class="lede">This isn't a contract &mdash; it's how we schedule a discovery call. Expect a reply within two business days.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid grid-2" style="align-items:start;">
      <div>
        <form data-inquiry-form>
          <div class="form-grid">
            <div>
              <label for="gs-name">Full name</label>
              <input id="gs-name" name="name" type="text" required>
            </div>
            <div>
              <label for="gs-email">Email address</label>
              <input id="gs-email" name="email" type="email" required>
            </div>
            <div>
              <label for="gs-project">Project type</label>
              <select id="gs-project" name="project_type">
                <option>New residential build</option>
                <option>Residential renovation</option>
                <option>Civic or public building</option>
                <option>Commercial or mixed-use</option>
                <option>Planning &amp; feasibility only</option>
                <option>Other</option>
              </select>
            </div>
            <div>
              <label for="gs-budget">Estimated construction budget</label>
              <select id="gs-budget" name="budget">
                <option>Under $250,000</option>
                <option>$250,000 &ndash; $750,000</option>
                <option>$750,000 &ndash; $2,000,000</option>
                <option>Over $2,000,000</option>
                <option>Not yet determined</option>
              </select>
            </div>
            <div class="full">
              <label for="gs-location">Site location</label>
              <input id="gs-location" name="location" type="text" placeholder="City, country">
            </div>
            <div class="full">
              <label for="gs-details">Tell us about the site and what you're hoping to build</label>
              <textarea id="gs-details" name="details" placeholder="Site size, current condition, program, timeline &mdash; whatever you have."></textarea>
            </div>
          </div>
          <button class="btn btn-primary" type="submit" style="margin-top:26px;">Submit Inquiry</button>
          <p class="form-note">Submitting this form does not create a client relationship or engage the practice. We'll follow up to schedule a discovery call.</p>
        </form>
        <div class="form-success">
          <strong>Thank you &mdash; your inquiry has been received.</strong>
          <p style="margin:8px 0 0;">A principal will review your project and follow up within two business days to schedule a discovery call.</p>
        </div>
      </div>

      <div>
        <div class="panel" style="margin-bottom:30px;">
          <span class="mono-label">WHAT HAPPENS NEXT</span>
          <h3>A short, honest first conversation</h3>
          <p>We review every inquiry personally. If your project is a fit, we'll schedule a 30-minute discovery call. If it isn't &mdash; wrong scale, wrong region, wrong timeline &mdash; we'll tell you that directly and, where we can, point you to a practice that's a better fit.</p>
        </div>
        <div class="panel">
          <span class="mono-label">PREFER TO TALK FIRST?</span>
          <h3>Reach a studio directly</h3>
          <p>See <a href="contact.html" style="color:#A9812C;">Contact</a> for direct lines to our Lagos, London and Toronto studios.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
